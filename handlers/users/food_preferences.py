from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ReplyKeyboardRemove
from keyboard.default import custom
from aiogram import types
from loader import dp


@dp.message_handler(Command("custom"))
async def start_customization(message: types.Message):
    await message.answer('Tap on the button'
                         "if you're agree that:", reply_markup=custom)


@dp.message_handler(Text(startswith="I'm"))
async def vegetarian_or_vegan(message: types.Message):
    await message.answer(f"Okey, you're{message.text[3:]}"
                         f"\nSomething else?")


@dp.message_handler(Text(startswith="I don't"))
async def i_will_die_if_i_eat(message: types.Message):
    await message.answer("Which kind of food"
                         " you can't eat?", reply_markup=ReplyKeyboardRemove())
