from config.config import BOT_TOKEN, ATTEMPTS
from userdata import *
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message

import random


''' Функции для игры'''


def get_random_number() -> int:
    return random.randint(1, 100)


''' Логика работы бота '''
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    if not message.from_user.id in users.keys:
        users[message.from_user.id] = User(in_game=False,
                                           secret_number=None,
                                           attempts=None,
                                           total_games=0,
                                           wins=0)
    print(*users, sep="\n")
    await message.answer('Привет! Я хочу сыграть с тобой в игру "Угадай число".\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправь команду /help')


@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\n'
                         f'Я загадываю число от 1 до 100, а тебе нужно его угадать.\n'
                         f'У тебя есть {ATTEMPTS} попыток.\n\n'
                         f'Доступные команды:\n'
                         f'/help - правила игры и список команд\n'
                         f'/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\n'
                         f'Давай сыграем?')


@dp.message(Command(commands=["stat"]))
async def process_stat_command(message: Message):
    await message.answer(f"@{message.from_user.username}, вот твоя статистика игр:\n"
                         f"Всего игр сыграно: {users[message.from_user.id].total_games}\n"
                         f"Побед: {users[message.from_user.id].wins}")
    await process_start_command(message)


@dp.message(Command(commands=["cancel"]))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]:
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом')
        users[message.from_user.id].in_game = False
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')


@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра', 'Играть', 'Хочу играть'], ignore_case=True))
async def process_positive_answer(message=Message):
    if not users[message.from_user.id].in_game:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
        users[message.from_user.id].in_game = True
        users[message.from_user.id].secret_number = get_random_number()
        users[message.from_user.id].attempts = ATTEMPTS
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')


@dp.message()
async def process_unknown_commands(message: Message):
    if users[message.from_user.id].in_game:
        await message.answer('Мы же сейчас с вами играем. '
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')


if __name__ == "__main__":
    dp.run_polling(bot)
