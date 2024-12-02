from keyboards.default.eng_btn import *
from keyboards.inline.eng_btn import *
from aiogram.dispatcher import FSMContext
from data.config import *
from utils.databace import *
from .start import *


@dp.message_handler(text="English 🇺🇸", state=UserState.language)
async def set_uz_langugae(message: types.Message):
    await save_language(message.from_user.id, "en")
    await message.answer("First, subscribe to our channel 😊", reply_markup=channel_btn_eng)
    await UserState.channel_follow.set()


@dp.callback_query_handler(text="check_subscription_eng", state=UserState.channel_follow)
async def check_subscription_callback(call: types.CallbackQuery):
    is_subscribed = await check_subscription(call.message.chat.id)

    if is_subscribed:
        await call.message.delete()
        await call.message.answer("Send your phone number 📞", reply_markup=phone_number_eng)
        await UserState.phone_number_eng.set()
    else:
        await call.message.answer("First, subscribe to our channel 😊", reply_markup=channel_btn_eng)


@dp.message_handler(state=UserState.phone_number_eng, content_types=types.ContentType.CONTACT)
async def set_phone_number(message: types.Message, state: FSMContext):
    await save_user_data(message.from_user.id, message.contact.full_name, message.from_user.username,
                         message.contact.phone_number)
    await message.answer("You have successfully registered ✅", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Choose:", reply_markup=menu_btn_eng)
    await state.finish()


@dp.message_handler(text="Recommend 📝")
async def set_recomand(message: types.Message):
    await message.answer("Send a picture of the price you want to recommend 📸",
                         reply_markup=types.ReplyKeyboardRemove())
    await UserState.tavsiya_qilmoq_eng.set()
    await record_stat(message.from_user.id)


@dp.message_handler(state=UserState.tavsiya_qilmoq_eng, content_types=types.ContentType.PHOTO)
async def set_tavsiya_qilmoq_photo(message: types.Message, state: FSMContext):
    fake_data[message.from_user.id]["photo_id"] = message.photo[-1].file_id
    await message.answer("The picture you sent has been accepted ✅")
    await message.answer("Now send text for picture 📝")


@dp.message_handler(state=UserState.tavsiya_qilmoq_eng, content_types=types.ContentType.TEXT)
async def set_tavsiya_qilmoq_text(message: types.Message, state: FSMContext):
    await message.answer("Your recommendation has been accepted✅\n\nYour opinion is very important to us!☺️")
    user_data = await check_user(message.from_user.id)
    username = ""
    if user_data[3] == None:
        username = ""
    else:
        username = user_data[3]
    caption = f"""
<code>Mijozning ma'lumotlari 👤:</code>

<b>Ismi:</b> {user_data[2]}
<b>Username:</b> @{username}
<b>Telefon raqami:</b> +{user_data[4]}

<b>{message.text}</b>
"""
    await bot.send_photo(chat_id=GROUP_ID, photo=fake_data[message.from_user.id]["photo_id"], caption=caption)
    await message.answer("Chooce:", reply_markup=menu_btn_eng)
    await state.finish()
