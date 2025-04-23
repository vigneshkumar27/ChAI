from beanie import Document,Indexed,init_beanie
import asyncio

from src.utils.mongodb import db_connection

class User(Document):
    name:str
    age:int

async def main():
    db = await db_connection()
    await init_beanie(database=db,document_models=[User])

    user1 = User(name="rtbtet",age=45)
    await user1.insert()


asyncio.run(main())
    
