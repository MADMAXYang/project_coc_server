from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)

database_chat_channel = client["chat-channel"]

