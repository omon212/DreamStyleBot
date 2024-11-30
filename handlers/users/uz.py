from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram import types
from states.user_state import UserState
from keyboards.default.uz_btn import phone_number_uz
from keyboards.inline.uz_btn import channel_btn
from data.config import CHANNEL_ID

async def check_subscription(user_id):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        return False

@dp.message_handler(text="Uzbek 🇺🇿", state=UserState.language)
async def set_uz_langugae(message: types.Message):
    await message.answer("Avval, kanalimizga obuna bo'ling 😊",reply_markup=channel_btn)
    await UserState.channel_follow.set()

@dp.callback_query_handler(text="check_subscription",state=UserState.channel_follow)
async def check_subscription_callback(call: types.CallbackQuery):
    is_subscribed = await check_subscription(call.message.chat.id)

    if is_subscribed:
        await call.message.delete()
        await call.message.answer("Telefon raqamingizni yuboring 📞",reply_markup=phone_number_uz)
        await UserState.phone_number.set()
    else:
        await call.message.answer("Avval, kanalimizga obuna bo'ling 😊",reply_markup=channel_btn)


@dp.message_handler(state=UserState.phone_number,content_types=types.ContentType.CONTACT)
async def set_phone_number(message: types.Message, state: FSMContext):
    await message.answer("Siz muvaffaqiyatli ro'yxatdan o'tdingiz ✅",reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Tanlang:")
