import os
import dotenv
dotenv.load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram import F

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []

        for word in message.text.split():
            normalized_word = word.replace(".", "").replace(",", "").strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))

        return {"numbers": numbers} if numbers else False


@dp.message(F.text.lower().startswith('найди числа'), NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.reply(text=f"Нашёл: {', '.join(str(num) for num in numbers)}")

@dp.message(F.text.lower().startswith('найди числа'))
async def pricess_if_not_numbers(message: Message):
    await message.reply(text="Не нашёл чисел...")


if __name__ == "__main__":
    dp.run_polling(bot)
