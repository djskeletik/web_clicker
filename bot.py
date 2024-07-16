import asyncio
import logging
import sys
import config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = config.token

dp = Dispatcher()

builder = InlineKeyboardBuilder()
builder.button(text="Открыть кликер", web_app=WebAppInfo(url="https://djskeletik.github.io/web_clicker/"))

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.reply("Привет! Нажми на кнопку, чтобы начать кликать:", reply_markup=builder.as_markup())

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())