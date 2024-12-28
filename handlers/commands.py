
from aiogram import types, Dispatcher
from config import bot
import os
import random

async def start_handler(message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Hello! Your Telegram ID is {message.from_user.id}"
    )
async def info_handler(message):
    await message.reply("Я бот для управления товарами и заказами. Вы можете:\n"
                            "- Добавлять товары (для сотрудников)\n"
                            "- Оформлять заказы\n"
                            "- Просматривать товары")

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])