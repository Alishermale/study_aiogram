import os
from aiogram import Bot, types
from dotenv import load_dotenv
from loader import dp


load_dotenv()
bot = Bot(os.getenv('BOT_TOKEN'))
admin_id = os.getenv('ADMIN_ID')


# admin
@dp.message_handler(commands='admin', user_id=admin_id)
async def admin(message: types.Message):
    await bot.send_message(message.chat.id, 'Hi! That message only for admins.')
