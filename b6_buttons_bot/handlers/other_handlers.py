from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU
from aiogram import F

from keyboards.other_keyboard import keyboard_1, kb_builder
from keyboards.common_buttons import common_keyboard
from keyboards.web_keyboard import web_keyboard

router: Router = Router()


@router.message(F.text.lower() == 'обычная')
async def process_common(message: Message):
    await message.answer(text='Клавиатура с обычными кнопками',
                         reply_markup=common_keyboard)


@router.message(F.text.lower() == 'веб')
async def process_web(message: Message):
    await message.answer(text='Открываю GitHub',
                         reply_markup=web_keyboard)



@router.message(F.text.lower() == 'вопрос')
async def process_question(message: Message):
    await message.answer(text="Чего кошки боятся больше?",
                         reply_markup=keyboard_1)


@router.message(F.text.lower() == 'собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(text='Да, несомненно, кошки боятся собак. '
                         'Но вы видели, как они боятся огурцов?')

@router.message(F.text.lower() == 'огурцов 🥒')
async def process_dog_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов '
                         'кошки боятся больше')


@router.message()
async def send_echo(message: Message):
    try:
        await message.copy_to(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
