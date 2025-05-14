import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from beanie import init_beanie
from src.models.model import Message,User,Threads
from datetime import datetime

# Test imports

uri = os.environ['mongo_uri']
db_name = os.environ['db']

async def db_connection():
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    await init_beanie(database=db,document_models=[Threads,Message,User])

async def insert_item(collection_name,insert_data):
    print()
    
async def delete_item(collection_name,delete_data):
    max()

async def update_item(collection_name,update_data):
    map()
async def get_item(collection_name,item_id):
    collection_name.find()
    User.find()
    return await collection_name.find().to_list()