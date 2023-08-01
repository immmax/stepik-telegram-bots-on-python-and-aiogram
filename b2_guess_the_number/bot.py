from config.config import BOT_TOKEN

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Я хочу сыграть с тобой в игру.")


@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("Есть вопросы? Я могу помочь тебе.")


@dp.message(Command(commands=["stat"]))
async def process_stat_command(message: Message):
    await message.answer(f"@{message.from_user.username}, вот твоя статистика игр:\n"
                         f"Всего сыграно игр: {0}\n"
                         f"Побед: {0}")

    await process_start_command(message)


@dp.message(Command(commands=["cancel"]))
async def process_cancel_command(message: Message):
    await message.answer("Игра прервана. :( Возвращайтесь.")


@dp.message()
async def process_unknown(message: Message):
    await message.answer("Не уверен, что это значит...")
    await process_start_command(message)


if __name__ == "__main__":
    dp.run_polling(bot)
