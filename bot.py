from config.token import BOT_TOKEN
import json

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


# "/start" command handler
async def process_start_command(message: Message):
    await message.answer("Hello!\nI'm Echo Bot.\nText me something.")


# "/help" command handler
async def process_help_command(message: Message):
    await message.answer("Text me something. As an answer "
                         "I'll send you your message.")


# photo handler
async def send_photo_echo(message: Message):
    # print(*message, sep="\n")
    await message.reply_photo(message.photo[0].file_id)


# other commands handler
async def send_echo(message: Message):
    try:
        await message.reply(text=message.text)
    except Exception as e:
        # print(*message, sep="\n")
        await message.reply(text=f"Я пока не могу обрабатывать "
                                 f"такие сообщения:\n{e}")

dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=["help"]))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)
