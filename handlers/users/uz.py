from loader import dp, bot
from aiogram import types
from states.user_state import UserState
from keyboards.default.uz_btn import phone_number_uz


@dp.message_handler(text="Uzbek 🇺🇿", state=UserState.language)
async def set_uz_langugae(message: types.Message):
    await message.answer("Avval, kanalimizga obuna bo'ling 😊",reply_markup=)
    await UserState.channel_follow.set()

@dp.message_handler(state=UserState.channel_follow)
async def get_phone_number(message: types.Message):
    await message.answer("Telefon raqamingizni yuboring 📞", reply_markup=phone_number_uz)
    # await UserState.language.set()