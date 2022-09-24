from aiogram import Bot, Dispatcher
from .config import token, parse_mode
from loguru import logger

# Telegram bot token
bot = Bot(token, parse_mode=parse_mode)

dp = Dispatcher(bot)
logger.info("Bot is starting")

