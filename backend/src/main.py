# from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from quart import Quart,request,jsonify

load_dotenv()

server = Quart("CHAI BACKEND")

@server.route("/", methods=["GET"])
async def root_route():
    return jsonify({"message":"received"})

server.run(port=5000)
    