from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU
from aiogram import F

from keyboards.other_keyboard import keyboard_1, kb_builder

router: Router = Router()


@router.message(F.text.lower() == 'вопрос')
async def process_question(message: Message):
    await message.answer(text="Чего кошки боятся больше?",
                         reply_markup=kb_builder.as_markup(
                            resize_keyboard=True))

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
