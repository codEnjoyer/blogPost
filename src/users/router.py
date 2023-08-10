from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from database import get_async_session
from users.crud import get_all_users
from users.models import User
from users.schemas import UserRead

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/protected_route")
async def protected_route(user: Annotated[User, Depends(current_user)]):
    return f"This is a protected route, {user.username}"


@router.get("/")
async def get_users(db: Annotated[AsyncSession, Depends(get_async_session)],
                    limit: int = 10,
                    offset: int = 0) -> list[UserRead]:
    users = await get_all_users(db, limit, offset)
    return list(users)


@router.get("/{user_id}")
async def get_user(user_id: int):
    pass


@router.get("/{user_id}/publications")
async def get_user_publications(user_id: int):
    pass


@router.get("/{user_id}/reactions")
async def get_user_reactions(user_id: int):
    pass
