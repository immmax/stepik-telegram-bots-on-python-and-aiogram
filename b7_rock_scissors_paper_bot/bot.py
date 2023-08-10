import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from keyboards.set_menu import set_main_menu

logger = logging.getLogger(__name__)



async def main():

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await set_main_menu(bot=bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('>>> Работаем!')
    asyncio.run(main())
