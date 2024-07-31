from pymongo import MongoClient
from config import Config

def list_databases_and_collections():
    client = MongoClient(Config.MONGODB_URI)

    # List all databases
    databases = client.list_database_names()
    print("Databases:")
    for db_name in databases:
        print(f"- {db_name}")

        # List all collections in the database
        db = client[db_name]
        collections = db.list_collection_names()
        print("  Collections:")
        for collection in collections:
            print(f"  - {collection}")

if __name__ == "__main__":
    list_databases_and_collections()
