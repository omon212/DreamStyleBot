from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni yuborish ☎️", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

menu_btn_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tavsiya qilmoq 📝")
        ],
    ],
    resize_keyboard=True
)
