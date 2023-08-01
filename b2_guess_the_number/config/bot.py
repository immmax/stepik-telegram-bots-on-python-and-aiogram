from config.token import BOT_TOKEN

from aiogram import Bot, Dispatcher

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()
