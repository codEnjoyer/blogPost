from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from database import get_async_session
from publications.crud import get_publication_by_id
from reactions.crud import get_all_reactions, get_user_reaction_to_publication
from reactions.schemas import ReactionRead, ReactionCreate, ReactionUpdate
from users.models import User

router = APIRouter(prefix="/publications", tags=["Reactions"])


@router.get("/{publication_id}/reactions")
async def get_reactions(publication_id: int,
                        db: Annotated[AsyncSession, Depends(get_async_session)],
                        limit: int = 20,
                        offset: int = 0) -> list[ReactionRead]:
    publication = await get_publication_by_id(db, publication_id)
    if not publication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    reactions = await get_all_reactions(publication, limit, offset)
    if not reactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Reactions was not found")
    return list(reactions)


@router.get("/{publication_id}/reaction")
async def get_my_reaction(publication_id: int,
                          user: Annotated[User, Depends(current_user)],
                          db: Annotated[AsyncSession, Depends(get_async_session)]) -> ReactionRead:
    publication = await get_publication_by_id(db, publication_id)
    if not publication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    reaction = await get_user_reaction_to_publication(publication, user.id)
    return reaction


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
