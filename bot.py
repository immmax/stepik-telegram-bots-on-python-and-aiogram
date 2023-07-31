from config.token import BOT_TOKEN
# import json

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
# from aiogram import F

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
    try:
        await bot(message.send_copy(chat_id=message.chat.id))
    except Exception as e:
        print(*message, sep="\n")
        await message.reply(text=f"Данный тип апдейтов не поддерживается "
                                 f"методом send_copy:\n{e}")


if __name__ == "__main__":
    dp.run_polling(bot)
