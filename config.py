from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

Admins = [795236182, ]
Staff = [795236182, 1111111111, 222222222, ]

storage = MemoryStorage()
bot = Bot(token='7923441200:AAFunsoW6KsAikGoketgWJqFvY58_8mh4c8')
dp = Dispatcher(bot,storage=storage)
