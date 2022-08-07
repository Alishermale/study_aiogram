from aiogram.dispatcher.filters.state import StatesGroup, State


class GetInfoAboutUser(StatesGroup):
    name = State()
    email = State()
    phone_number = State()
