from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    language = State()
    phone_number = State()
    channel_follow = State()
    phone_number_ru = State()
    language_ru = State()
    phone_number_eng = State()
    language_eng = State()

