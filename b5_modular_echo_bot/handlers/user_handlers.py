from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_celp_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
