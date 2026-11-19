from typing import Any, Sequence
from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.sql import Executable

from database.engine import async_session


class DatabaseRequests:
    def __init__(self, session_maker: async_sessionmaker[AsyncSession] = async_session):
        self.session_maker = session_maker

    async def add(self, instance: Any) -> None:
        async with self.session_maker() as session:
            async with session.begin():
                session.add(instance)

    async def add_all(self, instances: Sequence[Any]) -> None:
        async with self.session_maker() as session:
            async with session.begin():
                session.add_all(instances)

    async def select(self, query: Executable) -> Any:
        async with self.session_maker() as session:
            async with session.begin():
                result = await session.execute(query)
                return result.first()

    async def select_all(self, query: Executable) -> Sequence[Any]:
        async with self.session_maker() as session:
            async with session.begin():
                result = await session.execute(query)
                return result.all()

    async def update(self, query: Executable) -> None:
        async with self.session_maker() as session:
            async with session.begin():
                await session.execute(query)

    async def delete(self, query: Executable) -> None:
        async with self.session_maker() as session:
            async with session.begin():
                await session.execute(query)

    async def select_sql(self, raw_sql: str, params: dict | None = None) -> Sequence[Any]:
        async with self.session_maker() as session:
            async with session.begin():
                result = await session.execute(text(raw_sql), params or {})
                return result.all()

    async def execute_sql(self, raw_sql: str, params: dict | None = None) -> None:
        async with self.session_maker() as session:
            async with session.begin():
                await session.execute(text(raw_sql), params or {})


db_requests = DatabaseRequests()