from sqlalchemy import BigInteger, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Admin(Base):
    __tablename__ = 'db_admin_bot_users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    telegram_name: Mapped[str] = mapped_column(String, nullable=True)
