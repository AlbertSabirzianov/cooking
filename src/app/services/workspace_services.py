from sqlalchemy import select

from ..models.workspase_models import WorkSpace, Ingredient
from .db_session import async_session


async def get_workspaces_by_phone(phone: str) -> list[WorkSpace]:
    async with async_session() as session:
        stmt = select(WorkSpace).where(WorkSpace.user_phone == phone)
        result = await session.scalars(stmt)
        return result.fetchall()


