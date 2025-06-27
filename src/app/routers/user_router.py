from fastapi import APIRouter, Depends, HTTPException

from ..schema.user_schema import UserSchema, UserTokenSchema, UserGetSchema
from ..services.user_services import get_user_by_phone, get_password_hash, get_token_by_phone, get_phone_from_token, verify_password
from ..services.base import create_model
from ..models.user_models import User
from ..schema.responses import ErrorResponse, MessageResponse, TokenResponse
from ..dependencies.auth_dependencies import token_in_header

user_router = APIRouter()


@user_router.post(
    "/",
    responses={
        200:  {'model': MessageResponse},
        400:  {'model': ErrorResponse},
    }
)
async def post_user(user_schema: UserSchema):
    if await get_user_by_phone(user_schema.phone):
        raise HTTPException(status_code=400, detail=f"User with phone number {user_schema.phone} already exists")
    user_schema.password = get_password_hash(user_schema.password)
    await create_model(
        User(
            **user_schema.model_dump()
        )
    )
    return {"message": "user created!"}


@user_router.post(
    "/token",
    responses={
        400:  {'model': ErrorResponse},
        200:  {'model': TokenResponse},
    }
)
async def get_token(user_schema: UserTokenSchema):
    user = await get_user_by_phone(user_schema.phone)
    if not user:
        raise HTTPException(status_code=400, detail=f"User with phone {user_schema.phone} not exists")
    if not verify_password(user_schema.password, user.password):
        raise HTTPException(status_code=400, detail=f"Wrong Password!")
    return TokenResponse(token=get_token_by_phone(user.phone))


@user_router.get(
    "/",
    response_model=UserGetSchema,
    responses={
        400:  {'model': ErrorResponse},
        401:  {'model': ErrorResponse},
        200: {'model': UserGetSchema},
    }
)
async def get_user(token: str = Depends(token_in_header)):
    user = await get_user_by_phone(phone=get_phone_from_token(token))
    if not user:
        raise HTTPException(status_code=400, detail=f"User not exists")
    return user







