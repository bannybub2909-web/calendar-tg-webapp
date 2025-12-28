import asyncio
import json
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="📅 Записаться",
                    web_app=WebAppInfo(
                        url="https://bannybub2909-web.github.io/calendar-tg-webapp/"
                    )
                )
            ]
        ],
        resize_keyboard=True
    )

    await msg.answer(
        "Привет 👋\nНажми кнопку, чтобы записаться:",
        reply_markup=keyboard
    )

@dp.message(F.web_app_data)
async def web_app_data(msg: Message):
    data = json.loads(msg.web_app_data.data)

    date = data.get("date")
    text = data.get("text", "—")

    await msg.answer(
        "✅ Запись получена!\n\n"
        f"📅 Дата: {date}\n"
        f"📝 Комментарий: {text}"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
