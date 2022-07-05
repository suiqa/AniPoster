import asyncio
import logging
import os
from pygelbooru import Gelbooru
from pybooru import Danbooru
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from saucenao_api import SauceNao

# Токен бота, диспатчер и логирование
bot = Bot('token_here', parse_mode='HTML')

# Токен SauceNao
sauce = SauceNao('api_key_here')

# Токен Gelbooru
gelbooru = Gelbooru('api_key', 'user_id')

# Токен Danbooru
danbooru = Danbooru('danbooru', username='username', api_key='api_key_here')


async def main(dp: Dispatcher):
    @dp.message_handler(commands="start")
    async def start(message: types.Message):
        await message.reply("Image Poster for @neko_religion")

    # Обработка изображения и поиск на SauceNao
    @dp.message_handler(content_types=["photo"])
    async def download_photo(message: types.Message):
        await message.photo[-1].download(destination_file="temp.jpg")
        await message.reply("Поиск изображения по подходящим критериям.")
        with open("temp.jpg", 'rb') as img:
            results = sauce.from_file(img)
            for url in results[0].urls:
                if 'gelbooru.com' in url or 'konachan.net' in url:
                    await message.reply(f"Автор: {results[0].author}\nСсылка на изображение: {url}")
                    break
            else:
                await message.reply("Изображение по подходящим критериям не найдено.")

        os.remove("temp.jpg")

    # Пост картинки по id Gelbooru
    @dp.message_handler(commands="post_gel")
    async def post_gel(message: types.Message):
        post_id_gel = message.get_args()
        results_gel = await gelbooru.get_post(int(post_id_gel))
        tags_gel = ' '.join([f'#{r}' for r in results_gel.tags])
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        buttons = [
            types.InlineKeyboardButton(text="Full", url=results_gel.file_url),
        ]
        keyboard.add(*buttons)
        rating_gel = results_gel.rating
        for rating_gel in rating_gel:
            if rating_gel == 's':
                rating_gel = 'Safe 🟢'
            elif rating_gel == 'q':
                rating_gel = 'Questionable 🟡'
            elif rating_gel == 'e':
                rating_gel = 'Explicit 🔴'
            elif rating_gel == 'l':
                rating_gel = 'Safe 🟢'
        await bot.send_photo(chat_id=-1001646859181, photo=str(results_gel.file_url), caption=f'🏷 Tags: {tags_gel}\n🔗 Source: {results_gel.source}\n💮 Rating: {rating_gel}\n\n🆔 Gelbooru : {results_gel.id}', reply_markup=keyboard)

    # Пост картинки по id Danbooru
    @dp.message_handler(commands="post_dan")
    async def post_dan(message: types.Message):
        post_id_dan = message.get_args()
        results_dan = danbooru.post_show(int(post_id_dan))

        res = {}

        res['tags'] = ' '.join([f'#{r}' for r in results_dan['tag_string_general'].split()])
        res['id'] = results_dan['id']
        res['source'] = results_dan['source']
        res['rating'] = {'s': 'Safe 🟢', 'q': 'Questionable 🟡', 'e': 'Explicit 🔴', 'g': 'Safe 🟢'}.get(results_dan['rating'], f'error type - {results_dan["rating"]}')
        res['file_url'] = results_dan['file_url']

        txt = '🏷 Tags: {tags}\n🔗 Source: {source}\n💮 Rating: {rating}\n\n🆔 Danbooru : <code>{id}</code>'.format(**res)
        kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Full", url=res['file_url']))

        await bot.send_photo(chat_id=-1001646859181, photo=types.InputFile.from_url(res['file_url']), caption=txt, reply_markup=kb)

    # Обход блокировки бота
    @dp.errors_handler(exception=BotBlocked)
    async def error_bot_blocked(update: types.Update, exception: BotBlocked):
        print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
        return True

# Запуск бота
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()
    dp = Dispatcher(bot, loop=loop)
    executor.start_polling(dp, skip_updates=True, on_startup=main)
