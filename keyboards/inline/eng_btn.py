from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

channel_btn_eng = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="DreamStyle", url="https://t.me/dreamstayle"),
        ],
        [
            InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/dreamstyle__uz/"),
        ],
        [
            InlineKeyboardButton(text="Check ✅ ", callback_data="check_subscription_eng"),
        ]
    ]
)
