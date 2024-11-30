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
        [
            KeyboardButton(text="Настройки ⚙️")
        ]
    ],
    resize_keyboard=True
)
