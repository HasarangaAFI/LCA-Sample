import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_URI = os.getenv("MONGODB_URI")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    DATABASE_NAME = "LCADB"
    USER_COLLECTION = "Users"
