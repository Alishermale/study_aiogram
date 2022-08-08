from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states import GetInfoAboutUser
from keyboard.default import custom
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
