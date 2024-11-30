from aiogram import types
from loader import dp, bot
from states.user_state import UserState
from keyboards.default.eng_btn import *
from keyboards.inline.eng_btn import *
from aiogram.dispatcher import FSMContext
from data.config import *
from utils.databace import *
from .start import check_subscription


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
