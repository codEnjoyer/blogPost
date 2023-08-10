from datetime import datetime

from fastapi_users.schemas import BaseUserCreate, BaseUserUpdate, BaseUser


class UserRead(BaseUser[int]):
    registered_at: datetime


class UserCreate(BaseUserCreate):
    username: str


class UserUpdate(BaseUserUpdate):
    username: str | None
