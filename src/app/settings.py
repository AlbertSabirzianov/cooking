from pydantic_settings import BaseSettings


class DbSettings(BaseSettings):
    db_url: str = 'sqlite+aiosqlite:///cooking.db'


class AuthSettings(BaseSettings):
    secret_key: str
