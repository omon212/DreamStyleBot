from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send phone number ☎️", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

menu_btn_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Recommend 📝")
        ]
    ],
    resize_keyboard=True
)
