import logging
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from config import get_settings

settings = get_settings()


print("pbkdf2_sha256")
logging.error(f'pbkdf2_sha256')

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
logging.error(pwd_context)


def get_password_hash(password: str) -> str:
    try:
        logging.error(pwd_context)

        print(password)
        return pwd_context.hash(password)
    except:
        logging.error(pwd_context)

        print(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        print(plain_password)
        return pwd_context.verify(plain_password, hashed_password[:72])
    except:
        print(plain_password)
        logging.error(plain_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def decode_token(token: str) -> Optional[dict]:
    try:
        print(token)
        print(settings.SECRET_KEY, settings.ALGORITHM)
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
