from multiprocessing.sharedctypes import Value

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    if len(password) < 8:
        raise ValueError("password must be greater than 8 characters long")
    if len(password) > 64:
        raise ValueError("password must be less than 64 charecters")

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
