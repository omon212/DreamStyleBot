from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

channel_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="DreamStyle ",url="https://t.me/dreamstayle"),
        ],
        [
            InlineKeyboardButton(text="Tekshirish ✅ ",callback_data="check_subscription"),
        ]
    ]
)