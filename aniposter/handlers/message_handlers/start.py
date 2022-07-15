from aiogram import types
from loguru import logger
from aniposter.bot import dp


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply("Image Poster for @neko_religion")
