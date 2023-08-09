from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


button_1: KeyboardButton = KeyboardButton(text="Собак 🦮")
button_2: KeyboardButton = KeyboardButton(text="Огурцов 🥒")

keyboard_1: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]])
