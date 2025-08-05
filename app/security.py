from fastapi import Header, HTTPException, status
from app.config import get_settings

def verify_token(authorization: str = Header(...)):
    scheme, _, token = authorization.partition(" ")
    settings = get_settings()

    if scheme.lower() != "bearer" or token != settings.BEARER_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing Bearer token",
        )
    return token

