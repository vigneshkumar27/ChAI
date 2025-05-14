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
    # user1 = User(
    #     auth0_id="srtjrtyeyj",
    #     username="klarkin",
    #     email="lfnejrv@njebrt.oxm",
    #     auth_provider="oauth",
    #     created_at=datetime.utcnow(),
    #     updated_at=datetime.utcnow(),
    #     profile_picture="http://evhertvbr.com",
    #     bio="teyjhntyn",
    #     memories=['wrvbr','hethbr'],
    #     custom_instructions=['rhtbertb'],
    #     role=['user'],
    #     preferences={"theme":"dark","notification":True},
    #     age=1234,
    #     chat_threads=[PydanticObjectId("64c7b5e6f9f2d34b56c6c7c8"),PydanticObjectId("64c7b5e6f9f2d34b56c6c7c6")]
    # )
    # await user1.save()
    
    thread1 = Threads(
        user_id=PydanticObjectId("64c7b5e6f9f2d34b56c6c7c8"),
        title="ohuigbh",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        messages=[PydanticObjectId("64c7b5e6f9f2d34b56c6c7c8"),PydanticObjectId("64c7b5e6f9f2d34b56c6c7d4")]
    )
    
    message = Message(
        thread_id=PydanticObjectId("64c7b5e6f9f2d34b56c6c7c8"),
        created_at=datetime.utcnow(),
        sender="gbr",
        message_content="brtbrwtb"
    )
    await thread1.save()
    await message.save()


asyncio.run(main())
    
