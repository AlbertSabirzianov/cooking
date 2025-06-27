from typing import Optional

from sqlalchemy import select
from passlib.context import CryptContext
from jose import jwt

from .db_session import async_session
from ..models.user_models import User
from ..settings import AuthSettings

auth_settings = AuthSettings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_token_by_phone(phone: str) -> str:
    return jwt.encode({"phone": phone}, key=auth_settings.secret_key)


def get_phone_from_token(token: str) -> str:
    return jwt.decode(token=token, key=auth_settings.secret_key).get("phone")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def get_user_by_phone(phone: str) -> Optional[User]:
    async with async_session() as session:
        stmt = select(User).where(User.phone == phone)
        result = await session.scalars(stmt)
        return result.first()





