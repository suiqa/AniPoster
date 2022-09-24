from aniposter.handlers.message_handlers import start
from .handlers.errors_handler import *
from .config import config
from loguru import logger
from aniposter.bot import dp
from aiogram import executor

# Init logger
logger.add("out.log", backtrace=True, diagnose=True)

# Config stuff
channel_id = config["POSTER"]["channel_id"]
owner_id = config["POSTER"]["owner_id"]
if not channel_id or not owner_id:
    logger.error("Pls check POSTER config section")
    quit()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
