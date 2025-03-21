from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Update


class AdminCheckMiddleware(BaseMiddleware):
    def __init__(self, admins: list[int]):
        super().__init__()
        self.admins = admins

    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        tg_id = event.message.from_user.id
        if tg_id in self.admins:
            return await handler(event, data)
        else:
            pass
