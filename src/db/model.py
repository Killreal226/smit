from sqlalchemy import String, Column, Integer, Float, Date

from src.db.core import Base, engine
from src.config import db_config


class Tariff(Base):
    __tablename__ = db_config.db_table_name

    id = Column(Integer, primary_key=True, autoincrement=True)
    cargo_type = Column(String(32))
    rate = Column(Float)
    date = Column(Date, index=True)


async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
