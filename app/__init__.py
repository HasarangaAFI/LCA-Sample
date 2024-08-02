# # employee_management_system/app/__init__.py
# from fastapi import FastAPI
# from app.controllers import auth_controller

# def create_app():
#     app = FastAPI()

#     app.include_router(auth_controller.router)

#     return app
from fastapi import FastAPI
from app.controllers import auth_controller

def create_app() -> FastAPI:
    app = FastAPI()
    
    # Include routers
    app.include_router(auth_controller.router, prefix="/auth", tags=["auth"])
    
    return app
