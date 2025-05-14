# from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from quart import Quart,request,jsonify
from src.utils.handler_utils import get_all_users
from src.utils.logger import logger

load_dotenv()

server = Quart("CHAI BACKEND")

@server.route("/", methods=["GET"])
async def root_route():
    logger.info("Root route called execution")
    return jsonify({"message":"received"})

@server.route("/api/users", methods=["GET"])
async def get_users():
    logger.info("get all users api called")
    users = await get_all_users()
    logger.info(users)
    return jsonify({"users":users})
    

server.run(port=5000)
    