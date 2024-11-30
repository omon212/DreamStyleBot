from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.btn import btn
from loader import dp
from states.user_state import UserState

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"""
Assalomu alaykum birinchi tilni tanlang 🇺🇿

Hello, please choose your language 🇺🇸

Привет, пожалуйста, выберите ваш язык 🇷🇺
    """,reply_markup=btn)
    await UserState.kanal_follow.set()


