from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from data.config import ADMINS
from utils.extra_datas import make_title


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Hello World!")
