from pymongo import MongoClient

# Your MongoDB connection string
mongo_uri = "mongodb+srv://rumesh:cluster0@cluster0.sdus7hk.mongodb.net/?retryWrites=true&w=majority"

try:
    # Create a MongoDB client
    client = MongoClient(mongo_uri)
    
    # Connect to the database
    db = client.test  # 'test' is a placeholder database, you can use any database name

    # Perform a simple operation to check the connection
    server_info = client.server_info()  # This will throw an exception if the connection fails
    
    print("Connected to MongoDB server:")
    print(server_info)

except Exception as e:
    print("Unable to connect to the MongoDB server.")
    print(e)
