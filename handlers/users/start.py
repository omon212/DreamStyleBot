import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.btn import btn
from keyboards.default.eng_btn import menu_btn_eng
from keyboards.default.ru_btn import menu_btn_ru
from loader import dp, bot
from states.user_state import UserState
from utils.databace import check_user
from data.config import CHANNEL_ID
from keyboards.default.uz_btn import *

fake_data = {}

conn = sqlite3.connect('stats.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS stats
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   date DATE)''')

conn.commit()

async def record_stat(user_id):
    cursor.execute("INSERT INTO stats (user_id, date) VALUES (?, DATE('now'))", (user_id,))
    conn.commit()


@dp.message_handler(commands=['stats'])
async def show_stats(message: types.Message):
    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM stats")
    total_users = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM stats WHERE date = DATE('now')")
    today_users = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM stats")
    total_requests = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM stats WHERE date = DATE('now')")
    today_requests = cursor.fetchone()[0]
    text = f"📊 Botdan foydalanish statistikasi:\n" \
           f" ├ Jami foydalanuvchilar: {total_users}\n" \
           f" ├ Bugungi foydalanuvchilar: {today_users}\n" \
           f" ├ Jami so'rovlar: {total_requests}\n" \
           f" └ Bugungi so'rovlar: {today_requests}"
    await message.reply(text)


async def check_subscription(user_id):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        return False


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    user = await check_user(message.from_user.id)

    if user:
        if user[5] == "uz":
            await message.answer(f"Assalomu aleykum {user[2]}")
            await message.answer("Tanlang:", reply_markup=menu_btn_uz)
        elif user[5] == "ru":
            await message.answer(f"Привет {user[2]}")
            await message.answer("Выберите:", reply_markup=menu_btn_ru)
        elif user[5] == "en":
            await message.answer(f"Hello {user[2]}", reply_markup=menu_btn_eng)
            await message.answer("Choose:", )
    else:
        await message.answer(f"""
Assalomu alaykum birinchi tilni tanlang 🇺🇿

Hello, please choose your language 🇺🇸

Привет, пожалуйста, выберите ваш язык 🇷🇺
        """, reply_markup=btn)
        await UserState.language.set()
    await record_stat(message.from_user.id)
