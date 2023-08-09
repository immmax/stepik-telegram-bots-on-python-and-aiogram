from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

web_btn: KeyboardButton = KeyboardButton(text='Open GitHub',
                                             web_app=WebAppInfo(url='https://github.com/immmax'))

kb_builder.row(web_btn, width=1)

web_keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True,
                                                     one_time_keyboard=True)
