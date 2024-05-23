
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder



start_button_1 = KeyboardButton(text='* Начать Игру *')

keyboard_after_cancel = ReplyKeyboardMarkup(
    keyboard=[[start_button_1]],
    resize_keyboard=True)