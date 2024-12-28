
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
cancel_button = KeyboardButton("Cancel")
cancel_markup.add(cancel_button)

start_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
start_markup.add(KeyboardButton('/start'), KeyboardButton('/store'),
                 KeyboardButton('/info'), KeyboardButton('/send_products'))

submit = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
submit.add(KeyboardButton("Yes"), KeyboardButton('No'))