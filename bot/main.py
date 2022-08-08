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


# bot's customization
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


# echo
@dp.message_handler()
async def echo(message: types.Message):
    text = str(message['text'])
    await message.answer(text)


executor.start_polling(dp)
