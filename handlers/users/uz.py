import types
from aiogram.dispatcher import FSMContext

from keyboards.default.ru_btn import orqaga_btn_ru
from keyboards.inline.uz_btn import channel_btn
from data.config import *
from utils.databace import *
from .start import *


@dp.message_handler(text="Uzbek 🇺🇿", state="*")
async def set_uz_langugae(message: types.Message):
    await save_language(message.from_user.id, "uz")
    await message.answer("Avval, kanalimizga obuna bo'ling 😊", reply_markup=channel_btn)
    await UserState.channel_follow.set()


@dp.callback_query_handler(text="check_subscription", state=UserState.channel_follow)
async def check_subscription_callback(call: types.CallbackQuery):
    is_subscribed = await check_subscription(call.message.chat.id)

    if is_subscribed:
        await call.message.delete()
        await call.message.answer("Telefon raqamingizni yuboring 📞", reply_markup=phone_number_uz)
        await UserState.phone_number.set()
    else:
        await call.message.answer("Avval, kanalimizga obuna bo'ling 😊", reply_markup=channel_btn)


@dp.message_handler(state=UserState.phone_number, content_types=types.ContentType.CONTACT)
async def set_phone_number(message: types.Message, state: FSMContext):
    await save_user_data(message.from_user.id, message.contact.full_name, message.from_user.username,
                         message.contact.phone_number)
    await message.answer("Siz muvaffaqiyatli ro'yxatdan o'tdingiz ✅", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Tanlang:", reply_markup=menu_btn_uz)
    await state.finish()


@dp.message_handler(text="Tavsiya qilmoq 📝")
async def set_tavsiya_qilmoq(message: types.Message):

    try:
        del fake_data[message.from_user.id]
    except KeyError:
        pass  # This could mean the user did not have any previous data
    except Exception as e:
        print(f"Error: {e}")
    await message.answer("Tavsiya qilmoqchi bo'lgan narxsangizni rasmini yuboring 📸",
                         reply_markup=types.ReplyKeyboardRemove())
    await UserState.tavsiya_qilmoq.set()
    await record_stat(message.from_user.id)


@dp.message_handler(state=UserState.tavsiya_qilmoq, content_types=types.ContentType.PHOTO)
async def set_tavsiya_qilmoq_photo(message: types.Message, state: FSMContext):
    if message.from_user.id not in fake_data:
        fake_data[message.from_user.id] = {}
    fake_data[message.from_user.id]["photo_id"] = message.photo[-1].file_id

    await message.answer("Yuborgan rasmingiz qabul qilindi ✅")
    await message.answer("Endi rasm uchun matn yuboring 📝")


@dp.message_handler(state=UserState.tavsiya_qilmoq, content_types=types.ContentType.TEXT)
async def set_tavsiya_qilmoq_text(message: types.Message, state: FSMContext):
    # Check if the photo exists for the user
    if message.from_user.id not in fake_data or "photo_id" not in fake_data[message.from_user.id]:
        await message.answer("Iltimos, avval rasm yuboring 📸.")
        return

    await message.answer("Tavsiyangiz qabul qilindi ✅\n\nSizning fikringiz biz uchun juda muhim!☺️")
    user_data = await check_user(message.from_user.id)
    username = user_data[3] if user_data[3] else "Username mavjud emas"

    caption = f"""
<code>Mijozning ma'lumotlari 👤:</code> 
<b>Ismi:</b> {user_data[2]}
<b>Username:</b> @{username}
<b>Telefon raqami:</b> +{user_data[4]}


<b>{message.text}</b>
"""

    # Send the photo to the group
    await bot.send_photo(chat_id=GROUP_ID, photo=fake_data[message.from_user.id]["photo_id"], caption=caption)

    await message.answer("Tanlang:", reply_markup=menu_btn_uz)
    await state.finish()
