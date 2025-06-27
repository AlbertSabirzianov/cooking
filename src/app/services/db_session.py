from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from ..settings import DbSettings
from ..models.base import Base
from ..models.user_models import User
from ..models.workspase_models import WorkSpace, Ingredient

db_settings = DbSettings()

engine = create_async_engine(db_settings.db_url, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
