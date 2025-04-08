from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession

from db.requests import get_orders_list
from db import Order
from objects.objects import OrdersHistoryPage


logger = getLogger(__name__)


async def show_orders_page(sessionmaker: AsyncSession,
                           page: OrdersHistoryPage | None = None,
                           first: bool = False) -> None | OrdersHistoryPage:

    orders: list[Order] = await get_orders_list(sessionmaker)
    orders_num = len(orders)

    if first:
        page = OrdersHistoryPage()

    page.pages_num = orders_num // 10

    page.first_order_num = cur_order = page.current_page * 10

    if page.current_page == page.pages_num:
        page.last_order_num = orders_num
    else:
        page.last_order_num = (page.current_page + 1) * 10

    output_str = ''

    for order in orders[page.first_order_num: page.last_order_num]:
        cur_order += 1
        output_str += (f'{cur_order}. {order.created_at.strftime('%d.%m.%y %H:%M')} {order.service}\n'
                       f'   {order.name} {order.phone}\n')

    page.text_string = output_str

    if first:
        return page
