from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession

from lexicon.ru import answers
from keyboards.inline_keyboards import history_showing_kb
from calculations.show_history import show_orders_page
from objects.objects import FSMOrders
# from db.requests import drop_table_transactions


router = Router()
logger = getLogger(__name__)


@router.message(Command(commands='start'))
async def start_command(message: Message) -> None:
    await message.answer(text=answers['/start'])
    logger.info('User pressed command /start')


@router.message(Command(commands='help'))
async def help_command(message: Message) -> None:
    await message.answer(text=answers['/help'])
    logger.info('User pressed command /help')


@router.message(Command(commands='orders'))
async def history_command(message: Message, state: FSMContext, sessionmaker: AsyncSession) -> None:
    await state.set_state(FSMOrders.show)
    page = await show_orders_page(sessionmaker, first=True)
    await message.answer(
        text=page.text_string,
        reply_markup=history_showing_kb(
            page.current_page,
            page.pages_num,
            page.first_order_num,
            page.last_order_num)
        .as_markup()
    )
    logger.info('User pressed command /orders')


# @router.message(Command(commands='clear_db'))
# async def clear_db_command(message: Message, admin_id: int, sessionmaker: AsyncSession) -> None:
#     if message.from_user.id == admin_id:
#         await sessionmaker.run_sync(drop_table_transactions)
#         await message.answer(
#             text='Database cleared'
#         )
#     logger.info('User pressed command /drop_db')


@router.message(Command(commands='cancel'))
async def cancel_command(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.reply(text=answers[message.text])
    logger.info('User pressed command /cancel')
