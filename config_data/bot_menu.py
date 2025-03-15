from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.ru import command_menu


async def set_menu(bot: Bot):
    menu_commands: list = [
        BotCommand(command=com, description=desc)
        for com, desc in command_menu.items()
    ]
    await bot.set_my_commands(menu_commands)
