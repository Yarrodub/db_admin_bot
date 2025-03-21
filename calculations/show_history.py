from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession

from db.requests import get_orders_list
from db import Order

logger = getLogger(__name__)


async def show_orders_page(sessionmaker: AsyncSession,
                                 page: int | None = None,
                                 pages_num: int | None = None,
                                 changes: int | None = None) -> tuple[int, int, str]:
    output_str = ''

    recordings: list[Order] = await get_orders_list(sessionmaker)
    logger.info(f'HISTORY_SHOWING Showing transactions page: {page}/{pages_num}')

    if page is None:
        page = 0
        pages_num = len(recordings) // 10

    if changes:
        if 0 <= page + changes <= pages_num:
            page += changes

    if page == pages_num:
        last_on_page = len(recordings)
    else:
        last_on_page = (page + 1) * 10
    first_on_page = cur_trn = page * 10

    for order in recordings[first_on_page: last_on_page]:
        cur_trn += 1
        output_str += (f'{cur_trn}. {order.created_at} '
                       f'{order.service} {order.name} '
                       f'{order.phone}\n')

    return page, pages_num, output_str
