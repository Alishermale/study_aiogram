from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from keyboard.inline import action_in_market
from keyboard.inline.callback_market import market_callback
from loader import dp, bot

rating = [0, 0]


@dp.message_handler(Command('market'))
async def market(message: types.Message):
    await bot.send_photo(photo="https://upload.wikimedia.org/"
                               "wikipedia/commons/6/69/Banana.png",
                         chat_id=message.from_user.id,
                         caption=f'Banana\nRating {rating[0]}/{rating[1]}',
                         reply_markup=action_in_market)


@dp.callback_query_handler(market_callback.filter(item_name="Buy"))
async def buy_product(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Buy the Banana!")


@dp.callback_query_handler(market_callback.filter(item_name="Like"))
async def like_product(call: CallbackQuery):
    await call.answer(cache_time=60)
    rating[0], rating[1] = rating[0] + 1, rating[1] + 1
    await call.message.answer(f"Rating is risen.\nNow rating is {rating[0]}/{rating[1]}")


@dp.callback_query_handler(market_callback.filter(item_name="Dislike"))
async def dislike_product(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Rating is sank.\nNow rating is {rating[0]}/{rating[1]}")
    rating[1] = rating[1] + 1
