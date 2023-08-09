from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

buttons: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}')
                                 for i in range(10)]

kb_builder.row(*buttons)

button_1: KeyboardButton = KeyboardButton(text="Собак 🦮")
button_2: KeyboardButton = KeyboardButton(text="Огурцов 🥒")

keyboard_1: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]],
    resize_keyboard=True,
    one_time_keyboard=True)
