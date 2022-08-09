from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboard.inline.callback_data import buy_callback


choice = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Buy apples!",
            callback_data=buy_callback.new(item_name='Apple')
        ),
        InlineKeyboardButton(
            text="Buy oranges!",
            callback_data=buy_callback.new(item_name='Orange')
        )
    ],
    [
        InlineKeyboardButton(
            text='Cancel',
            callback_data='Cancel'
        )
    ]
])
# apple
apples_keyboard = InlineKeyboardMarkup()
APPLES_LINK = "https://en.wikipedia.org/wiki/Apple"
apples_link = InlineKeyboardMarkup(text="Info about apple.", url=APPLES_LINK)

apples_keyboard.insert(apples_link)

# orange
oranges_keyboard = InlineKeyboardMarkup()
ORANGES_LINK = "https://en.wikipedia.org/wiki/Orange_(fruit)"
oranges_link = InlineKeyboardMarkup(text="Info about orange.", url=ORANGES_LINK)

oranges_keyboard.insert(oranges_link)
