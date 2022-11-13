import asyncio

from aiogram.utils.callback_data import CallbackData
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputFile)
from aniposter.bot import bot, dp
from aniposter.config import channel_id, saucenao_key
from loguru import logger
from saucenao_api import AIOSauceNao
from saucenao_api.errors import LongLimitReachedError, ShortLimitReachedError
from aniposter.__main__ import owner_id

SauceNaoPost = CallbackData("Act",
    "title",
    "similarity",
    "author",
    "urls",
    )

saucenao_buff = {}

@dp.message_handler(content_types=['photo'], user_id=owner_id)
async def saucenao_handler(message):
    async with AIOSauceNao(saucenao_key) as aio:
        file_ = await bot.download_file_by_id(message.photo[-1].file_id)
        results = await aio.from_file(file_)

    logger.debug(results[0])
    sauce_item = results[0]
    inline_btn = InlineKeyboardMarkup()
    inline_btn.add(InlineKeyboardButton("📥", 
                    callback_data="saucenao"
        )
    )
    
    string = f"<b>Request limits (per 30 seconds limit)</b>: <code>{results.short_remaining}</code>\n<b>Request limits (per day limit)</b>: <code>{results.long_remaining}</code>\n"
    
    string = f"<b>Similarity</b>: <code>{sauce_item.similarity}</code>\n\n"
    string += f"<b>Title</b>: <code>{sauce_item.title}</code>\n"
    string += f"<b>Author</b>: <code>{sauce_item.author}</code>\n"
    string += f"<b>Urls</b>: {' '.join(sauce_item.urls)}\n"

    
    message = await bot.send_photo(chat_id=message.chat.id, caption=string, reply_markup=inline_btn, photo=sauce_item.thumbnail, reply_to_message_id=message.message_id)
    saucenao_buff[message.message_id] = sauce_item


@dp.callback_query_handler(text="saucenao")
async def send_callback_handler(callback_query: CallbackQuery):
    saucenao = saucenao_buff[callback_query.message.message_id]
    string = f"<b>Title</b>: <code>{saucenao.title}</code>\n"
    string += f"<b>Author</b>: <code>{saucenao.author}</code>\n"
    string += f"<b>Urls</b>: {' '.join(saucenao.urls)}\n"

    await bot.send_photo(channel_id, callback_query.message.reply_to_message.photo[-1].file_id, string)

    await callback_query.answer(
        text="OK.",
        show_alert=True
    )

    # Delete Art from buffer
    del saucenao_buff[callback_query.message.message_id]
