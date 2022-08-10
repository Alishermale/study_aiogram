from random import randint

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import MediaGroup, InputFile

from loader import dp, bot


@dp.message_handler(content_types='photo')
async def catch_photo(message: types.Message):
    await message.photo[-1].download()
    await message.answer("Your photo is downloaded")


@dp.message_handler(content_types='video')
async def catch_video(message: types.Message):
    await message.video.download()
    await message.answer("Your video is downloaded")


@dp.message_handler(Command("get_photo"))
async def get_photo(message: types.Message):
    random_file = randint(1, 5)
    photo_bytes = InputFile(path_or_bytesio=f"photos/file_{random_file}.jpg")
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_bytes,
                         caption="Do you wanna else?\n/more_photos")


@dp.message_handler(Command("get_video"))
async def get_photo(message: types.Message):
    random_file = randint(6, 10)
    video_bytes = InputFile(path_or_bytesio=f"videos/file_{random_file}.mp4")
    await bot.send_video(chat_id=message.from_user.id,
                         video=video_bytes,
                         caption="Do you wanna else?\n/more_videos")


@dp.message_handler(Command("more_photos"))
async def get_more_photos(message: types.Message):
    album = MediaGroup()
    for number in range(1, 6):
        photo_bytes = InputFile(path_or_bytesio=f"photos/file_{number}.jpg")
        album.attach_photo(photo_bytes)
    await message.answer_media_group(media=album)


@dp.message_handler(Command("more_videos"))
async def get_more_videos(message: types.Message):
    album = MediaGroup()
    for number in range(6, 10):
        videoo_bytes = InputFile(path_or_bytesio=f"videos/file_{number}.mp4")
        album.attach_video(videoo_bytes)
    await message.answer_media_group(media=album)
