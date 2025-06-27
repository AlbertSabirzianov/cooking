from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    phone: str
    address: str
    email: str
    password: str


class UserTokenSchema(BaseModel):
    phone: str
    password: str


class UserGetSchema(BaseModel):
    name: str
    phone: str
    address: str
    email: str