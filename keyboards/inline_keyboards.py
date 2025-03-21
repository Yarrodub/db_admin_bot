from logging import getLogger

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.ru import other_buttons

logger = getLogger(__name__)

back_button = InlineKeyboardButton(text=other_buttons['back'], callback_data='Back')


def create_orders_list_kb(page: int, pages_num: int) -> InlineKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.add(back_button)
    kb.row(InlineKeyboardButton(text='<<', callback_data=f'{page},{pages_num},first'),
           InlineKeyboardButton(text='<', callback_data=f'{page},{pages_num},previous'),
           InlineKeyboardButton(text=f'{page + 1}/{pages_num + 1}', callback_data=f'{page},{pages_num},page'),
           InlineKeyboardButton(text='>', callback_data=f'{page},{pages_num},next'),
           InlineKeyboardButton(text='>>', callback_data=f'{page},{pages_num},last'))
    return kb
