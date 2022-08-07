from bot import *


load_dotenv()
bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
admin_id = os.getenv('ADMIN_ID')


# admin
@dp.message_handler(commands='admin', user_id=admin_id)
async def admin(message: types.Message):
    await bot.send_message(message.chat.id, 'Hi! That message only for admins.')


@dp.message_handler(Command('form'))
async def start_sum(message: types.Message):
    await message.answer("Tell me your name")
    await GetInfoAboutUser.first()


@dp.message_handler(state=GetInfoAboutUser.name)
async def first_dig(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer('Great. Now tell me your email')
    await state.update_data(answer1=answer)
    await GetInfoAboutUser.next()


@dp.message_handler(state=GetInfoAboutUser.email)
async def second_dig(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Awesome! Last thing is you "
                         "phone number")
    await GetInfoAboutUser.next()


@dp.message_handler(state=GetInfoAboutUser.phone_number)
async def second_dig(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = data.get('answer2')
    answer = message.text
    await state.update_data(answer3=answer)
    await message.answer("Success! Your answers is"
                         f"\n{answer1}\n{answer2}\n{answer}")
    await state.finish()



# echo
@dp.message_handler()
async def echo(message: types.Message):
    text = str(message['text'])
    await message.answer(text)


executor.start_polling(dp)
