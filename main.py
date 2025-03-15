import asyncio

from logging import config, getLogger
from aiogram import Bot, Dispatcher

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from log_config.settings import logging_config
from config_data.bot_menu import set_menu
from config_data.config_reader import get_config, BotConfig, DbConfig
from middlewares import DbSessionMiddleware, TrackAllUsersMiddleware

from handlers import get_routers


config.dictConfig(logging_config)
logger = getLogger(__name__)


async def main():
    bot_config = get_config(BotConfig, 'bot')
    db_config = get_config(DbConfig, 'db')

    logger.info('Starting bot')

    engine = create_async_engine(
        url=str(db_config.dsn),
        echo=db_config.is_echo,
        pool_pre_ping=True
    )

    async with engine.begin() as conn:
        await conn.execute(text('SELECT 1'))

    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    dp = Dispatcher(admin_id=bot_config.admin_id)
    dp.update.outer_middleware(DbSessionMiddleware(sessionmaker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())

    dp.include_routers(*get_routers())

    bot = Bot(token=bot_config.token.get_secret_value())

    await set_menu(bot)
    await dp.start_polling(bot)


asyncio.run(main())
