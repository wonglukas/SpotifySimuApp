from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["musicapp"]
users_collection = db["users"]
listening_history_collection = db["listening_history"]

if __name__ == "__main__":
    app.run(port=5000)
