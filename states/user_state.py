from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    language = State()
    phone_number = State()
    channel_follow = State()
