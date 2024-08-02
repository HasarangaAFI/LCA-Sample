# from app import create_app
# import uvicorn
# app = create_app()

# if __name__ == "__main__":
    
#     uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI
from app.controllers import auth_router

def create_app() -> FastAPI:
    app = FastAPI()
    
    # Include routers
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    
    return app

app = create_app()
