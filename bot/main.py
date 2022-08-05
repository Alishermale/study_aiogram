from bot import *


load_dotenv()
bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
admin_id = os.getenv('ADMIN_ID')


# admin
@dp.message_handler(commands='admin', user_id=admin_id)
async def admin(message: types.Message):
    await bot.send_message(message.chat.id, 'Hi! That message only for admins.')


@dp.message_handler(Command('sum'))
async def start_sum(message: types.Message):
    await message.answer("You're open calculator\n"
                         "Tell me first number")
    await Summ.first()


@dp.message_handler(state=Summ.dig1)
async def first_dig(message: types.Message, state: FSMContext):
    try:
        answer = int(message.text)
    except ValueError:
        await message.answer('Try to use digits')
        first_dig()
    await state.update_data(answer1=answer)
    await message.answer('Now second digit')
    await Summ.next()


@dp.message_handler(state=Summ.dig2)
async def second_dig(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    try:
        answer2 = int(message.text)
    except ValueError:
        await message.answer('Try to use digits')
        second_dig()
    await message.answer(f'{answer1} + {answer2} = {answer1 + answer2}')
    await state.finish()


# echo
@dp.message_handler()
async def echo(message: types.Message):
    text = str(message['text'])
    await message.answer(text)


executor.start_polling(dp)
