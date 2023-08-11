from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from database import get_async_session
from reactions.schemas import ReactionRead, ReactionCreate, ReactionUpdate
from users.models import User

router = APIRouter(prefix="/publications", tags=["Reactions"])


@router.get("/{publication_id}/reactions")
async def get_reactions(publication_id: int,
                        db: Annotated[AsyncSession, Depends(get_async_session)],
                        limit: int = 20,
                        offset: int = 0) -> list[ReactionRead]:
    pass


@router.get("/{publication_id}/reaction")
async def get_my_reaction(publication_id: int,
                          user: Annotated[User, Depends(current_user)],
                          db: Annotated[AsyncSession, Depends(get_async_session)]) -> ReactionRead | None:
    pass


@router.post("/{publication_id}/reaction")
async def post_reaction(publication_id: int,
                        reaction: ReactionCreate,
                        user: Annotated[User, Depends(current_user)],
                        db: Annotated[AsyncSession, Depends(get_async_session)]) -> ReactionRead:
    pass


@router.delete("/{publication_id}/reaction")
async def delete_reaction(publication_id: int,
                          user: Annotated[User, Depends(current_user)],
                          db: Annotated[AsyncSession, Depends(get_async_session)]) -> ReactionRead:
    pass


@router.patch("/{publication_id}/reaction")
async def patch_reaction(publication_id: int,
                         reaction: ReactionUpdate,
                         user: Annotated[User, Depends(current_user)],
                         db: Annotated[AsyncSession, Depends(get_async_session)]) -> ReactionRead:
    pass
