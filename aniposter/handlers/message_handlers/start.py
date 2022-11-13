from aiogram import types
from loguru import logger
from aniposter.bot import dp
from aniposter.config import start_text

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply(start_text)
