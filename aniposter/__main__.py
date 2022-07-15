from .bot import dp
from aiogram import executor

from .handlers.message_handlers import *
from .handlers.errors_handler import *

from loguru import logger

# Init logger
logger.add("out.log", backtrace=True, diagnose=True)
logger.info("Bot is starting")


executor.start_polling(dp)
