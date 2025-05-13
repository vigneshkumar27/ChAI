import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import asyncio

# Test imports

uri = os.environ['mongo_uri']
db_name = os.environ['db']
async def db_connection():
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    db = client["chai_db"]
    return db

if __name__ == "__main__":     
    async def find_one():
        db = await db_connection()
        document = await db['Users'].find_one({"i": {"$lt": 1}})
        print(document)
    async def insert_one():
        db = await db_connection()
        document = {"key": "value"}
        await db['Users'].insert_one(document)
    
    asyncio.run(insert_one())