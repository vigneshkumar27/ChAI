from beanie import Document,Indexed,init_beanie,PydanticObjectId
from dotenv import load_dotenv
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, AnyUrl
from datetime import datetime
from datetime import datetime
import asyncio

load_dotenv()

from src.utils.mongodb import db_connection

class UserPreference(BaseModel):
    theme:str
    notification:bool

class User(Document):
    auth0_id:str = Indexed(unique=True)
    username:str
    email:EmailStr = Indexed(unique=True)
    auth_provider:str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    profile_picture:AnyUrl
    bio:str
    memories:List[str] = Field(default_factory=list)
    custom_instructions:List[str] = Field(default_factory=list)
    role:List[str] = Field(default_factory=list)
    preferences:Optional[UserPreference] = None
    age:int
    chat_threads:List[PydanticObjectId] = Field(default_factory=list)
    
class Threads(Document):
    user_id:PydanticObjectId
    title:str
    created_at:datetime = Field(default_factory=datetime.utcnow) 
    updated_at:Optional[datetime] = None
    messages:List[PydanticObjectId] = Field(default_factory=list)
class Message(Document):
    thread_id:PydanticObjectId
    created_at:datetime = Field(default_factory=datetime.utcnow) 
    edited:Optional[datetime] = None
    parent_id:Optional[PydanticObjectId] = None
    sender:str
    message_content:str

async def main():
    db = await db_connection()
    await init_beanie(database=db,document_models=[User, Threads, Message])
    
    users = await User.find()
    print(users)


asyncio.run(main())
    
