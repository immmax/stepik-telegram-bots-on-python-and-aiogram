from config.config import BOT_TOKEN

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# "/start" command handler
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Hello!\nI'm Echo Bot.\nText me something.")

# "/help" command handler
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("Text me something. As an answer "
                         "I'll send you your message.")

# other commands handler
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

if __name__ == "__main__":
    dp.run_polling(bot)
