from aniposter.bot import dp
from aiogram import types
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, Unauthorized
from loguru import logger


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    logger.warning(
        f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}"
    )


@dp.errors_handler(exception=ChatNotFound)
async def error_bot_chat_not_found(update: types.Update, exception: ChatNotFound):
    logger.error(
        f"Вы точно добавили меня в этот чат? \nСообщение: {update}\nОшибка: {exception}"
    )


@dp.errors_handler(exception=Unauthorized)
async def error_bot_unauthorized(update: types.Update, exception: Unauthorized):
    logger.error(
        f"Вы точно добавили меня в этот чат? \nСообщение: {update}\nОшибка: {exception}"
    )
