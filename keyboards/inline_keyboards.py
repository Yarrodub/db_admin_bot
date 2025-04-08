from logging import getLogger

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.ru import other_buttons

logger = getLogger(__name__)

back_button = InlineKeyboardButton(text=other_buttons['back'], callback_data='Back')


def history_showing_kb(page: int, pages_num: int, first_num: int, last_num: int) -> InlineKeyboardBuilder:
    kb = InlineKeyboardBuilder()

    current_page = f'{page},{pages_num}'

    # half_num = round((last_num - first_num)/2)

    kb.add(back_button)
    kb.row(InlineKeyboardButton(text='<<', callback_data=f'{current_page},first'),
           InlineKeyboardButton(text='<', callback_data=f'{current_page},previous'),
           InlineKeyboardButton(text=f'{page + 1}/{pages_num + 1}', callback_data=f'{current_page},page'),
           InlineKeyboardButton(text='>', callback_data=f'{current_page},next'),
           InlineKeyboardButton(text='>>', callback_data=f'{current_page},last'))
    # kb.row(*[InlineKeyboardButton(text=f'{num}', callback_data=f'{num}')
    #          for num in range(first_num + 1, first_num +  half_num +  1)])
    # kb.row(*[InlineKeyboardButton(text=f'{num}', callback_data=f'{num}')
    #          for num in range(first_num +  half_num +  1, last_num + 1)])
    return kb
