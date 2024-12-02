from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер телефона ☎️", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

menu_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рекомендовать 📝")
        ],
    ],
    resize_keyboard=True
)

orqaga_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад 🔙")
        ]
    ],
    resize_keyboard=True
)
