
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from app.models.user import User
# from app.dto.user_dto import UserDTO
# from app.dao.user_dao import UserDAO
# from config import Config
# from passlib.context import CryptContext

# # Use bcrypt for hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class AuthService:
#     def __init__(self, dao: UserDAO):
#         print("Initializing AuthService")
#         self.dao = dao

#     def hash_password(self, password: str) -> str:
#         print(f"Hashing password for: {password}")
#         return pwd_context.hash(password)

#     def verify_password(self, plain_password: str, hashed_password: str) -> bool:
#         print(f"Verifying password for: {plain_password}")
#         return pwd_context.verify(plain_password, hashed_password)

#     def register_user(self, username: str, email: str, password: str):
#         print(f"Registering user: {username}")
#         hashed_password = self.hash_password(password)
#         user = {"username": username, "email": email, "hashed_password": hashed_password}
#         print(f"Storing hashed password: {hashed_password}")
#         self.dao.create_user(user)
#         return UserDTO(username=username, email=email)

#     def authenticate_user(self, username: str, password: str):
#         print(f"Authenticating user: {username}")
#         user = self.dao.get_user_by_username(username)
#         if user:
#             print(f"User found: {user}")
#         else:
#             print("User not found")
#         if user and self.verify_password(password, user["hashed_password"]):
#             return UserDTO(username=user["username"], email=user["email"])
#         return None

#     def create_access_token(self, data: dict, expires_delta: timedelta = None):
#         print("Creating access token")
#         to_encode = data.copy()
#         if expires_delta:
#             expire = datetime.utcnow() + expires_delta
#         else:
#             expire = datetime.utcnow() + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
#         to_encode.update({"exp": expire})
#         encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
#         return encoded_jwt
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.models.user import User
from app.dto.user_dto import UserDTO
from app.dao.user_dao import UserDAO
from config import Config
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, dao: UserDAO):
        print("Initializing AuthService")
        self.dao = dao

    def hash_password(self, password: str) -> str:
        print(f"Hashing password for: {password}")
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        print(f"Verifying password for: {plain_password}")
        return pwd_context.verify(plain_password, hashed_password)

    def register_user(self, username: str, email: str, password: str) -> UserDTO:
        print(f"Registering user: {username}")
        hashed_password = self.hash_password(password)
        user = User(username=username, email=email, hashed_password=hashed_password)
        print(f"Storing user: {user}")
        self.dao.create_user(user.dict())
        return UserDTO(username=user.username, email=user.email)

    def authenticate_user(self, username: str, password: str) -> UserDTO:
        print(f"Authenticating user: {username}")
        user_data = self.dao.get_user_by_username(username)
        if not user_data:
            print("User not found")
            return None
        user = User(**user_data)
        if self.verify_password(password, user.hashed_password):
            return UserDTO(username=user.username, email=user.email)
        return None

    def create_access_token(self, data: dict, expires_delta: timedelta = None) -> str:
        print("Creating access token")
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
        return encoded_jwt
