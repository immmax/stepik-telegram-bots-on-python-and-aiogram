from config.config import BOT_TOKEN, ATTEMPTS
from userdata import *
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

import random


''' Функции для игры'''


def get_random_number() -> int:
    return random.randint(1, 100)


''' Логика работы бота '''
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    if not message.from_user.id in users:
        users[message.from_user.id] = User(username=message.from_user.username,
                                           in_game=False,
                                           secret_number=None,
                                           attempts=None,
                                           total_games=0,
                                           wins=0)
    print(users)
    await message.answer('Привет!\nЯ хочу сыграть с тобой в игру "Угадай число".\n'
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
    if users[message.from_user.id].in_game:
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом')
        users[message.from_user.id].in_game = False
        users[message.from_user.id].total_games += 1
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')


@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра', 'играть', 'хочу играть']))
async def process_positive_answer(message=Message):
    if not users[message.from_user.id].in_game:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
        users[message.from_user.id].in_game = True
        users[message.from_user.id].secret_number = get_random_number()
        users[message.from_user.id].attempts = ATTEMPTS
        print(users[message.from_user.id])
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')

@dp.message(F.text.lower.in_(['нет', 'не хочу', 'в другой раз', 'не', 'не буду']))
async def process_negative_answer(message: Message):
    if not users[message.from_user.id].in_game:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if users[message.from_user.id].in_game:
        if int(message.text) == users[message.from_user.id].secret_number:
            await message.answer('Ура!!! Вы угадали число!\n\n'
                                 'Может, сыграем еще?')
            users[message.from_user.id].in_game = False
            users[message.from_user.id].total_games += 1
            users[message.from_user.id].wins += 1
        elif int(message.text) > users[message.from_user.id].secret_number:
            await message.answer('Мое число меньше')
            users[message.from_user.id].attempts -= 1
        elif int(message.text) < users[message.from_user.id].secret_number:
            await message.answer('Мое число больше')
            users[message.from_user.id].attempts -= 1

        if users[message.from_user.id].attempts == 0:
            await message.answer(f'К сожалению, у вас больше не осталось '
                                 f'попыток. Вы проиграли :(\n\nМое число '
                                 f'было {users[message.from_user.id].secret_number}\n\nДавайте '
                                 f'сыграем еще?')
            users[message.from_user.id].in_game = False
            users[message.from_user.id].total_games += 1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')
    print(users[message.from_user.id])


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
