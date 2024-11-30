from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

channel_btn_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="DreamStyle", url="https://t.me/dreamstayle"),
        ],
        [
            InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/dreamstyle__uz/"),
        ],
        [
            InlineKeyboardButton(text="Проверка ✅", callback_data="check_subscription_ru"),
        ]
    ]
)
