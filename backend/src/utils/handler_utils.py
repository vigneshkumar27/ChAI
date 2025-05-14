from src.utils.db_operations import get_item
from src.utils.logger import logger

async def get_all_users():
    logger.info("werrt")
    users = await get_item("User",None)
    return users