from src.models.model import Message,User,Threads
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from beanie import init_beanie
import asyncio
import os



uri = os.environ['mongo_uri']
db_name = os.environ['db']

async def db_connection():
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    await init_beanie(database=db,document_models=[Threads,Message,User])
    

    
async def main():
    await db_connection()
    users = await User.find().to_list()
    print(users)
    
asyncio.run(main())