from aiogram import types
from loader import dp, bot
from states.user_state import UserState
from keyboards.default.ru_btn import *
from keyboards.inline.ru_btn import *
from aiogram.dispatcher import FSMContext
from data.config import *
from utils.databace import *
from .start import check_subscription


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
