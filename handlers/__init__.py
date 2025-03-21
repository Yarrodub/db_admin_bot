from aiogram import Router

from handlers.command_handlers import router as command_router
from handlers.history_handlers import router as history_router


def get_routers() -> list[Router]:
    return [command_router, history_router]
