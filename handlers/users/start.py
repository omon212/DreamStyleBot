from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.btn import btn
from loader import dp, bot
from states.user_state import UserState
from utils.databace import check_user
from data.config import CHANNEL_ID
from keyboards.default.uz_btn import *


async def check_subscription(user_id):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        return False


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await check_user(message.from_user.id)
    if user:
        if user[5] == "uz":
            await message.answer(f"Assalomu aleykum {user[2]}")
            await message.answer("Tanlang:", reply_markup=menu_btn_uz)
        elif user[5] == "ru":
            await message.answer(f"Привет {user[2]}")
            await message.answer("Выберите:", reply_markup=menu_btn_uz)
        elif user[5] == "en":
            await message.answer(f"Hello {user[2]}")
            await message.answer("Choose:", )
    else:
        await message.answer(f"""
Assalomu alaykum birinchi tilni tanlang 🇺🇿

Hello, please choose your language 🇺🇸

Привет, пожалуйста, выберите ваш язык 🇷🇺
        """, reply_markup=btn)
        await UserState.language.set()
