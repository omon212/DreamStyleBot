import types

from keyboards.default.ru_btn import *
from keyboards.inline.ru_btn import *
from aiogram.dispatcher import FSMContext
from data.config import *
from utils.databace import *
from .start import *


@dp.message_handler(text="Русский 🇷🇺", state=UserState.language)
async def set_uz_langugae(message: types.Message):
    await save_language(message.from_user.id, "ru")
    await message.answer("Для начала подпишитесь на наш канал 😊", reply_markup=channel_btn_ru)
    await UserState.channel_follow.set()


@dp.callback_query_handler(text="check_subscription_ru", state=UserState.channel_follow)
async def check_subscription_callback(call: types.CallbackQuery):
    is_subscribed = await check_subscription(call.message.chat.id)

    if is_subscribed:
        await call.message.delete()
        await call.message.answer("Отправьте свой номер телефона 📞", reply_markup=phone_number_ru)
        await UserState.phone_number_ru.set()
    else:
        await call.message.answer("Для начала подпишитесь на наш канал 😊", reply_markup=channel_btn_ru)


@dp.message_handler(state=UserState.phone_number_ru, content_types=types.ContentType.CONTACT)
async def set_phone_number(message: types.Message, state: FSMContext):
    await save_user_data(message.from_user.id, message.contact.full_name, message.from_user.username,
                         message.contact.phone_number)
    await message.answer("Вы успешно зарегистрировались ✅", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Выбирать:", reply_markup=menu_btn_ru)
    await state.finish()


@dp.message_handler(text="Рекомендовать 📝")
async def set_tavsiya_qilmoq(message: types.Message):
    try:
        del fake_data[message.from_user.id]
    except:
        pass
    await message.answer("Отправьте фото цены, которую хотите порекомендовать 📸",
                         reply_markup=types.ReplyKeyboardRemove())
    await UserState.tavsiya_qilmoq_photo_ru.set()
    await record_stat(message.from_user.id)


@dp.message_handler(state=UserState.tavsiya_qilmoq_photo_ru, content_types=types.ContentType.PHOTO)
async def set_tavsiya_qilmoq_photo(message: types.Message, state: FSMContext):
    if message.from_user.id not in fake_data:
        fake_data[message.from_user.id] = {}
    fake_data[message.from_user.id]["photo_id"] = message.photo[-1].file_id
    await message.answer("Отправленное вами изображение принято. ✅")
    await message.answer("Теперь отправьте текст для изображения 📝", reply_markup=types.ReplyKeyboardRemove())
    await UserState.tavsiya_qilmoq_text_ru.set()

@dp.message_handler(state=UserState.tavsiya_qilmoq_text_ru, content_types=types.ContentType.TEXT)
async def set_tavsiya_qilmoq_text_ru(message: types.Message, state: FSMContext):
    await message.answer("Ваша рекомендация принята ✅\n\nВаше мнение очень важно для нас!☺️")
    user_data = await check_user(message.from_user.id)
    username = ""
    if user_data[3] == None:
        username = "Имя пользователя не существует"
    else:
        username = user_data[3]
    caption = f"""
<code>Информация о клиенте 👤:</code>

<b>Имя:</b> {user_data[2]}
<b>Имя пользователя:</b> @{username}
<b>Номер телефона:</b> +{user_data[4]}

<b>{message.text}</b>
"""
    await bot.send_photo(chat_id=GROUP_ID, photo=fake_data[message.from_user.id]["photo_id"], caption=caption)
    await message.answer("Выберите:", reply_markup=menu_btn_ru)
    await state.finish()


