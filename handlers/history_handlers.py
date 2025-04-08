from logging import getLogger

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from objects.objects import FSMOrders, OrdersHistoryPage
from lexicon.ru import answers
from keyboards.inline_keyboards import history_showing_kb
from calculations.show_history import show_orders_page

router = Router()
logger = getLogger(__name__)


@router.callback_query(StateFilter(FSMOrders.show), F.data != 'Back')
async def orders_pagination(callback: CallbackQuery, sessionmaker: AsyncSession) -> None:
    data = callback.data

    page = OrdersHistoryPage(*data.split(','))

    await show_orders_page(sessionmaker, page)

    if not page.same_text:
        await callback.message.edit_text(
            text=page.text_string,
            reply_markup=history_showing_kb(page.current_page,
                                            page.pages_num,
                                            page.first_order_num,
                                            page.first_order_num)
            .as_markup()
        )
    else:
        await callback.answer(
            text='Нажмите другую кнопку'
        )
    logger.info(f'HISTORY_HANDLERS: User pressed button with data: {data}')


@router.callback_query(StateFilter(FSMOrders), F.data == 'Back')
async def back_button_pressed(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_text(
        text=answers['/start']
    )
    await state.clear()
    logger.info(f'User pressed back button')

