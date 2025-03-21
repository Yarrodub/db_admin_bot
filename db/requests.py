from typing import cast

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import joinedload

from db import Order, Admin


# def drop_table_transactions(
#         session: Session
# ):
#     Base.metadata.drop_all(bind=session.get_bind())
#     Base.metadata.create_all(bind=session.get_bind())
#     await session.commit()

async def get_orders_list(
        session: AsyncSession
) -> list[Order]:
    stmt = (select(Order)
            .order_by(Order.created_at.desc())
            .limit(100))
            # .options(joinedload(Order.name)))
    result = await session.execute(stmt)
    orders = result.scalars().all()
    orders = cast(list[Order], orders)
    return orders

async def get_admins_list(
        session: AsyncSession
) -> list[int]:
    stmt = select(Admin.telegram_id)
    result = await session.execute(stmt)
    admins = result.scalars().all()
    admins = cast(list[int], admins)
    return admins
