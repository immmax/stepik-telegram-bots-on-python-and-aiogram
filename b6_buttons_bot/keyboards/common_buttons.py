from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType
from aiogram.types import KeyboardButtonRequestUser, KeyboardButtonRequestChat

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

contact_btn: KeyboardButton = KeyboardButton(text='Send phone',
                                             request_contact=True)
location_btn: KeyboardButton = KeyboardButton(text='Send location',
                                              request_location=True)
poll_btn: KeyboardButton = KeyboardButton(text='Create poll',
                                          request_poll=KeyboardButtonPollType(type='regular'))
# user_btn: KeyboardButton = KeyboardButton(text='Send chat',
#                                           request_chat=KeyboardButtonRequestChat())
# chat_btn: KeyboardButton = KeyboardButton(text='Send user',
#                                           request_user=KeyboardButtonRequestUser())

kb_builder.row(contact_btn, location_btn, poll_btn, width=1)


common_keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True,
                                                     one_time_keyboard=True)
