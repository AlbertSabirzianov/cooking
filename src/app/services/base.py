from typing import TypeVar, Type, Optional

from sqlalchemy import select

from .db_session import async_session

T = TypeVar('T')


async def create_model(model) -> None:
    async with async_session() as session:
        session.add(model)
        await session.commit()


async def delete_model(model) -> None:
    async with async_session() as session:
        await session.delete(model)
        await session.commit()


async def get_model_by_id(model: Type[T], id: int) -> Optional[T]:
    async with async_session() as session:
        stmt = select(model).where(model.id == id)
        result = await session.scalars(stmt)
        return result.first()
