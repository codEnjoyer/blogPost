from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Query

from publications.schemas import PublicationRead
from reactions.schemas import ReactionRead
from users.crud import (
    get_all_users, get_user_by_id, get_all_user_publications, get_all_user_reactions,
    update_user_by_id, delete_user_by_id)
from users.schemas import UserRead, UserUpdate
from utils.types import AsyncDBSession, UserID, CurrentUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_users(db: AsyncDBSession,
                    limit: Annotated[int, Query(ge=0, le=10 ** 3)] = 10,
                    offset: Annotated[int, Query(ge=0, le=10 ** 6)] = 0) -> list[UserRead]:
    users = await get_all_users(db, limit, offset)
    return list(users)


@router.get("/{user_id}")
async def get_user(user_id: UserID,
                   db: AsyncDBSession) -> UserRead:
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User was not found")
    return user


@router.get("/{user_id}/publications")
async def get_user_publications(db: AsyncDBSession,
                                user_id: UserID) -> list[PublicationRead]:
    publications = await get_all_user_publications(db, user_id)
    if not publications:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User was not found")
    return list(publications)


@router.get("/{user_id}/reactions")
async def get_user_reactions(db: AsyncDBSession,
                             user_id: int) -> list[ReactionRead]:
    reactions = await get_all_user_reactions(db, user_id)
    if not reactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User was not found")
    return list(reactions)


@router.patch("/me")
async def update_current_user(db: AsyncDBSession,
                              user: CurrentUser,
                              user_update: UserUpdate) -> UserRead:
    user = await update_user_by_id(db, user.id, user_update)
    return user


@router.delete("/me")
async def delete_current_user(db: AsyncDBSession,
                              user: CurrentUser) -> UserRead:
    user = await delete_user_by_id(db, user.id)
    return user
