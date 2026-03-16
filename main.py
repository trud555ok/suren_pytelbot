import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command                #CommandStart для обработки команды /start
from aiogram.utils import markdown                              # помошник для формирования настроек текста
from  aiogram.enums import ParseMode                        #простые названия разметок
from config import BOT_TOKEN

dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f'Привет, {message.from_user.full_name}' )

@dp.message(Command('help'))
async def handle_help(message: types.Message):
    # text = "Я простой бот. \nОтправь мне сообщение."
    # entities_bolt = types.MessageEntity(
    #     type="bold",
    #     offset=len('Я простой бот. \nОтправь '),
    #     length=3,
    # )
    # entities = [entities_bolt]
    # await message.answer(text=text, entities=entities)
    text = "Я простой бот\\. \nОтправь *мне* сообщение\\!"
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)

@dp.message()
async def echo_message(message: types.Message):
    # await bot.send_message(chat_id=message.chat.id, text='Start procesing...') #простое сообщение
    # await bot.send_message(                     #простое сообщение
    #     chat_id=message.chat.id,
    #     text='Wait a second...',
    #     reply_to_message_id=message.message_id,         #указываем на какое сообщ ответить с упоминанием его
    # )
    #
    # await message.answer(text=message.text) #простой ответ
    # if message.text.startswith('/'):      если сообщение начинается с ....   -- но что бы не делать такие проверки
    #     pass  --- пишем свою функцию на /start
    try:
        await message.send_copy(chat_id=message.chat.id)    #send_copy - отправить копию любого формата
    except TypeError:
        await message.reply(text='якась хрень')

#     проверка или есть текст
    if message.text:
        await message.reply(text=message.text, entities=message.entities)  #ответ с указанием на что отвечаем
        #entities=message.entities   - отправит теже настройки текста (жирный, италик...)
    elif message.sticker:
        await message.reply_sticker(sticker=message.sticker.file_id)

        await message.bot.send_sticker(         #простая отправка стикера   message.bot - вызывает bot
            chat_id=message.chat.id,
            sticker=message.sticker.file_id,
        )
    else:
        await message.reply(text='что это?')  # ответ с указанием на что отвечаем



async def main():
    logging.basicConfig(level=logging.INFO)  #что б видеть все логи, DEBUG или INFO
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)    #опрашиваем телегу на наличие сообщений. в start_polling можно передавать несколько ботов!


if __name__ == "__main__":
    asyncio.run(main())