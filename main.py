import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from get_answer import get_answer_from_gpt
from openai import OpenAI

from resourses import bot_token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        gpt_answer = get_answer_from_gpt(message.text)
        await message.answer(gpt_answer)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(bot_token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
