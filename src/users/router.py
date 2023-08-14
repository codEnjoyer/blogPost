from fastapi import APIRouter

from publications.schemas import PublicationRead
from reactions.schemas import ReactionRead
from users.crud import (
    get_all_users, get_user_by_id, get_all_user_publications, get_all_user_reactions,
    update_user_by_id, delete_user_by_id)
from users.exceptions import UserNotFoundException
from users.schemas import UserRead, UserUpdate
from utils.types import AsyncDBSession, PathID, CurrentUser, QueryDBLimit, QueryDBOffset

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_users(db: AsyncDBSession,
                    limit: QueryDBLimit = 10,
                    offset: QueryDBOffset = 0) -> list[UserRead]:
    users = await get_all_users(db, limit, offset)
    return list(users)


@router.get("/{user_id}", name="Get User Info")
async def get_user(user_id: PathID,
                   db: AsyncDBSession) -> UserRead:
    user = await get_user_by_id(db, user_id)
    if not user:
        raise UserNotFoundException(user_id=user_id)
    return user


@router.get("/{user_id}/publications", tags=["Publications"], name="Get Publications of User")
async def get_user_publications(db: AsyncDBSession,
                                user_id: PathID) -> list[PublicationRead]:
    publications = await get_all_user_publications(db, user_id)
    if not publications:
        raise UserNotFoundException(user_id=user_id)
    return list(publications)


@router.get("/{user_id}/reactions", tags=["Reactions"], name="Get Reactions of User")
async def get_user_reactions(db: AsyncDBSession,
                             user_id: PathID) -> list[ReactionRead]:
    reactions = await get_all_user_reactions(db, user_id)
    if not reactions:
        raise UserNotFoundException(user_id=user_id)
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
