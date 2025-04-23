import asyncio
import os
from dotenv import load_dotenv 
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

load_dotenv()

uri = os.environ['mongo_uri']
db_name = os.environ['db']
print(uri)
async def db_connection():
    # Set the Stable API version when creating a new client
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    db = client["test_database"]
    return db