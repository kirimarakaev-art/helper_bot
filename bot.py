import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import common, survey
from database import create_db

async def main():
    logging.basicConfig(level=logging.INFO)

    # 1. Сначала создаем базу данных
    await create_db()

    # 2. Инициализируем бота
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    # 3. Подключаем роутеры
    dp.include_router(common.router)
    dp.include_router(survey.router)

    # 4. Запускаем
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())