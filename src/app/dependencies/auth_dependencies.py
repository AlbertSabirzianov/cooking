from fastapi import HTTPException, status, Header

from ..services.user_services import get_phone_from_token, get_user_by_phone


def token_in_header(token: str = Header()):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token must be provided"
        )
    try:
        get_phone_from_token(token=token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="token is not valid!"
        )
    return token


async def user_by_token(token: str = Header()):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token must be provided"
        )
    try:
        phone = get_phone_from_token(token=token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="token is not valid!"
        )

    return await get_user_by_phone(phone)
