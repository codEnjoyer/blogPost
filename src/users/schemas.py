from datetime import datetime

from fastapi_users.schemas import BaseUserCreate, BaseUserUpdate


class BaseUser:
    username: str


class UserRead(BaseUser):
    registered_at: datetime
    pass


class UserCreate(BaseUser, BaseUserCreate):
    pass


class UserUpdate(BaseUser, BaseUserUpdate):
    username: str | None
