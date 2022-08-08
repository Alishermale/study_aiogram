from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

custom = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="I'm vegan."),
            KeyboardButton(text="I'm vegetarian."),
        ],
        [
            KeyboardButton(text="I don't like some food. "
                                "\nI have an allergy."),
        ],
    ],
    resize_keyboard=True
)
