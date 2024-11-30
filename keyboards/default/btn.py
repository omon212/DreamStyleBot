from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uzbek 🇺🇿"),
            KeyboardButton(text="English 🇺🇸"),
            KeyboardButton(text="Русский 🇷🇺")
        ]
    ],
    resize_keyboard=True
)


