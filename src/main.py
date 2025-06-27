from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app.settings import DbSettings
from app.routers.user_router import user_router
from app.routers.workspace_router import workspace_router
from app.services.db_session import create_tables


def create_app() -> FastAPI:
    DbSettings()
    fastapi_app = FastAPI()

    fastapi_app.include_router(user_router, prefix="/users", tags=["auth"])
    fastapi_app.include_router(workspace_router, prefix="/workspace", tags=["workspace"])
    # fastapi_app.include_router(api_router)

    @fastapi_app.on_event("startup")
    async def startup_event():
        await create_tables()

    return fastapi_app


app = create_app()
