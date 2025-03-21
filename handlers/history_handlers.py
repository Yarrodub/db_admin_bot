from logging import getLogger

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from objects.objects import FSMOrders
from lexicon.ru import answers
from keyboards.inline_keyboards import create_orders_list_kb
from calculations.show_history import show_orders_page

router = Router()
logger = getLogger(__name__)


@router.callback_query(StateFilter(FSMOrders.show))
async def transaction_pagination(callback: CallbackQuery, state: FSMContext, sessionmaker: AsyncSession) -> None:
    data = callback.data

    if data == 'Back':
        await callback.message.edit_text(
            text=answers['/start']
        )
        await state.clear()
        logger.info(f'User pressed back button')

    page, pages_num, data, = data.split(',')
    changes = 0

    if data == 'previous':
        changes = -1

    elif data == 'next':
        changes = 1

    elif data == 'last':
        page = pages_num

    elif data == 'first':
        page = 0

    page, pages_num, txt = await show_orders_page(sessionmaker,
                                                  int(page),
                                                  int(pages_num),
                                                  changes)

    await callback.message.edit_text(
        text=txt,
        reply_markup=create_orders_list_kb(page, pages_num).as_markup()
    )
    logger.info(f'HISTORY_HANDLERS: User pressed button with data: {data}')
