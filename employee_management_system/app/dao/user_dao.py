# # employee_management_system/app/dao/user_dao.py
# from pymongo import MongoClient
# from app.models.user import User
# from config import Config

# class UserDAO:
#     def __init__(self, uri: str = Config.MONGODB_URI):
#         self.client = MongoClient(uri)
#         self.db = self.client['LCADB']  # Use the correct database
#         self.collection = self.db['Users']  # Use the correct collection

#     def find_by_username(self, username: str):
#         user_data = self.collection.find_one({"username": username})
#         return User(**user_data) if user_data else None

#     def save_user(self, user: User):
#         result = self.collection.insert_one(user.dict(by_alias=True))
#         user.id = result.inserted_id
#         return user
from pymongo import MongoClient
from config import Config

class UserDAO:
    def __init__(self, uri: str = Config.MONGODB_URI):
        self.client = MongoClient(uri)
        self.db = self.client[Config.DATABASE_NAME]
        self.collection = self.db[Config.USER_COLLECTION]

    def create_user(self, user_data):
        return self.collection.insert_one(user_data)

    def get_user_by_username(self, username):
        return self.collection.find_one({"username": username})

