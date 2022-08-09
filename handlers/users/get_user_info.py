from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states import GetInfoAboutUser


@dp.message_handler(Command('form'))
async def get_info_from_user(message: types.Message):
    await message.answer("Tell me your name")
    await GetInfoAboutUser.first()


@dp.message_handler(state=GetInfoAboutUser.name)
async def get_name(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer('Great. Now tell me your email')
    await state.update_data(answer1=answer)
    await GetInfoAboutUser.next()


@dp.message_handler(state=GetInfoAboutUser.email)
async def get_email(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Awesome! Last thing is you "
                         "phone number")
    await GetInfoAboutUser.next()


@dp.message_handler(state=GetInfoAboutUser.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = data.get('answer2')
    answer = message.text
    await state.update_data(answer3=answer)
    await message.answer("Success! Your answers is"
                         f"\n{answer1}\n{answer2}\n{answer}")
    await state.finish()
