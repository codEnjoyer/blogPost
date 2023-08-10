from datetime import datetime

from fastapi_users.schemas import BaseUserCreate, BaseUserUpdate, BaseUser


class CustomUser:
    username: str


class UserRead(BaseUser[int], CustomUser):
    registered_at: datetime


class UserCreate(BaseUserCreate, CustomUser):
    pass


class UserUpdate(BaseUserUpdate):
    username: str | None = None
