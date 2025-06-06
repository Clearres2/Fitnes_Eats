import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = '8141049018:AAGs72zhul9vIklBCI6KaynItCuOV8EkfO8'


dp = Dispatcher()

@dp.message(CommandStart)
async def command_brone_handler(message: Message) -> None:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Списки еды с рецептами и калориями",
                    web_app=WebAppInfo(url='https://clearres2.github.io/Fitnes_Eats/'),
                )
            ]
        ]
    )
    await message.answer(text='Бот Еды', reply_markup=markup)

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
