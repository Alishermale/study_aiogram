from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery
from keyboard.inline.callback_data import buy_callback
from keyboard.inline.choice_buttons import choice, apples_keyboard, oranges_keyboard
from loader import dp


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer("You can buy apples or oranges\n"
                         "If you don't need anything "
                         "press cancel.", reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="Apple"))
async def buying_apple(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("You're bought an apples",
                              reply_markup=apples_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="Orange"))
async def buying_orange(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("You're bought an orange",
                              reply_markup=oranges_keyboard)


@dp.callback_query_handler(Text(equals='Cancel'))
async def buying_orange(call: CallbackQuery):
    await call.message.answer("Goodbye!")
