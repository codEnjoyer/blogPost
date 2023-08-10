from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from database import get_async_session
from publications.schemas import Publication
from reactions.schemas import Reaction
from users.crud import get_all_users, get_user_by_id, get_all_user_publications, get_all_user_reactions
from users.models import User
from users.schemas import UserRead

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/protected_route")
async def protected_route(user: Annotated[User, Depends(current_user)]):
    return f"This is a protected route, {user}"


@router.get("/")
async def get_users(db: Annotated[AsyncSession, Depends(get_async_session)],
                    limit: int = 10,
                    offset: int = 0) -> list[UserRead]:
    users = await get_all_users(db, limit, offset)
    return list(users)


@router.get("/{user_id}")
async def get_user(db: Annotated[AsyncSession, Depends(get_async_session)],
                   user_id: int) -> UserRead:
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User was not found")
    return user


@router.get("/{user_id}/publications")
async def get_user_publications(db: Annotated[AsyncSession, Depends(get_async_session)],
                                user_id: int) -> list[Publication]:
    publications = await get_all_user_publications(db, user_id)
    if not publications:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User was not found")
    return list(publications)


@router.get("/{user_id}/reactions")
async def get_user_reactions(db: Annotated[AsyncSession, Depends(get_async_session)],
                             user_id: int) -> list[Reaction]:
    reactions = await get_all_user_reactions(db, user_id)
    if not reactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User was not found")
    return list(reactions)
