from aniposter.bot import dp, bot
from aiogram import types
from loguru import logger
from imageboard.booru import Booru, Gelbooru
from imageboard.yandere import Moebooru
from aiogram.types import InputFile
from aniposter.__main__ import owner_id, channel_id

booru, yandere, gelbooru = Booru(), Moebooru(), Gelbooru()

# rating_dict = {"s": "Safe 🟢", "q": "Questionable 🟡", "e": "Explicit 🔴", "g": "Safe 🟢", "sensitive": "Explicit 🔴", "general": "General 🟢"}

async def send_post(results: dict):
    tags = "".join("#" + tag_item + " " for tag_item in results.tag.split())
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Full", url=results.file_url),
    ]
    keyboard.add(*buttons)

    await bot.send_photo(
        chat_id=channel_id,
        photo=InputFile.from_url(results.sample_url),
        caption=f'🏷 Tags: {tags}\n🔗 Source: {results.source}\n\n🆔 : {results.id}',
        reply_markup=keyboard,
    )

@dp.message_handler(commands="yandere", user_id=owner_id)
async def post_yan(message: types.Message):
    post_id = message.get_args()
    results = await yandere.getByid(int(post_id))
    if not results:
        return await message.reply("No photo")
    
    await send_post(results)

@dp.message_handler(commands="danbooru", user_id=owner_id)
async def post_dan(message: types.Message):
    post_id = message.get_args()
    print("efg")
    results = await booru.getByid(int(post_id))
    if not results:
        return await message.reply("No photo")
    
    await send_post(results)

@dp.message_handler(commands="gelbooru", user_id=owner_id)
async def post_gel(message: types.Message):
    post_id = message.get_args()
    results = await gelbooru.getByid(int(post_id))
    if not results:
        return await message.reply("No photo")
    
    await send_post(results)

    
