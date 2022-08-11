from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboard.inline.callback_market import market_callback


action_in_market = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Buy!',
            callback_data=market_callback.new(item_name='Buy')
        )
    ],
    [
        InlineKeyboardButton(
            text="👍",
            callback_data=market_callback.new(item_name='Like')
        ),
        InlineKeyboardButton(
            text="👎",
            callback_data=market_callback.new(item_name='Dislike')
        )
    ],
    [
        InlineKeyboardButton(
            text='Share it!',
            callback_data='Send to friends'
        )
    ]
])
