from aniposter.bot import dp, bot
from aiogram import types
from loguru import logger
from imageboard.booru import Booru
from imageboard.yandere import Moebooru

booru = Booru()
yandere = Moebooru()
rating_dict = {"s": "Safe 🟢", "q": "Questionable 🟡", "e": "Explicit 🔴", "g": "Safe 🟢"}


@dp.message_handler(commands="post_yan")
async def post_yan(message: types.Message):
    post_id = message.get_args()
    results = await yandere.getByid(int(post_id))
    if not results:
        return await message.reply("No photo")

    tags = "".join("#" + tag_item + " " for tag_item in results.tag.split())
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Full", url=results.file_url),
    ]
    keyboard.add(*buttons)

    await bot.send_photo(
        chat_id=-1001649461490,
        photo=str(results.file_url),
        caption=f'🏷 Tags: {tags}\n🔗 Source: {results.source}\n💮 Rating: {rating_dict.get(results.rating, f"error type - {results.rating}")}\n\n🆔 Yandere : {results.id}',
        reply_markup=keyboard,
    )
