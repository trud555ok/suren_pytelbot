import asyncio
import logging
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = '7830152931:AAGe1xmx1BW_q9eIld3mDlg0eOBiziKmPmY'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_message(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Start procesing...') #простое сообщение
    await bot.send_message(                     #простое сообщение
        chat_id=message.chat.id,
        text='Wait a second...',
        reply_to_message_id=message.message_id,         #указываем на какое сообщ ответить с упоминанием его
    )

    await message.answer(text=message.text) #простой ответ
    await message.reply(text=message.text)  #ответ с указанием на что отвечаем


async def main():
    logging.basicConfig(level=logging.INFO) #что б видеть все логи, DEBUG или INFO
    await dp.start_polling(bot)    #опрашиваем телегу на наличие сообщений. в start_polling можно передавать несколько ботов!


if __name__ == "__main__":
    asyncio.run(main())