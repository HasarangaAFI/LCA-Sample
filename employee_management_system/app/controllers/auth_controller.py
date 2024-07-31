from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from app.services.auth_service import AuthService
from app.dto.user_dto import UserDTO
from app.dao.user_dao import UserDAO
from config import Config
from pydantic import BaseModel
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def get_auth_service() -> AuthService:
    print("Getting AuthService instance")
    dao = UserDAO(uri=Config.MONGODB_URI)
    return AuthService(dao=dao)

class UserRegister(BaseModel):
    user: UserDTO
    password: str

@router.post("/register", response_model=UserDTO)
def register(data: UserRegister, auth_service: AuthService = Depends(get_auth_service)):
    print("Register endpoint called")
    user = data.user
    password = data.password
    print(f"Received user: {user}")
    print(f"Received password: {password}")
    return auth_service.register_user(user.username, user.email, password)

@router.post("/token", response_model=dict)
def login(form_data: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends(get_auth_service)):
    print("Login endpoint called")
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
