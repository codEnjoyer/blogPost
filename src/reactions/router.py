from fastapi import APIRouter, HTTPException, status
from publications.crud import get_publication_by_id
from reactions.crud import (get_all_reactions, get_user_reaction_to_publication,
                            create_reaction, delete_reaction_from_db, update_reaction)
from reactions.schemas import ReactionRead, ReactionCreate
from utils.types import AsyncDBSession, QueryDBLimit, QueryDBOffset, PathID, CurrentUser

router = APIRouter(prefix="/publications", tags=["Reactions"])


@router.get("/{publication_id}/reactions")
async def get_reactions(publication_id: PathID,
                        db: AsyncDBSession,
                        limit: QueryDBLimit = 20,
                        offset: QueryDBOffset = 0) -> list[ReactionRead]:
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
async def get_my_reaction(publication_id: PathID,
                          user: CurrentUser,
                          db: AsyncDBSession) -> ReactionRead:
    publication = await get_publication_by_id(db, publication_id)
    if not publication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    reaction = await get_user_reaction_to_publication(publication, user.id)
    return reaction


@router.post("/{publication_id}/reaction")
async def post_reaction(publication_id: PathID,
                        reaction: ReactionCreate,
                        user: CurrentUser,
                        db: AsyncDBSession) -> ReactionRead:
    publication = await get_publication_by_id(db, publication_id)
    if publication.id == user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="You can't react to your own publication")
    if not publication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    reaction_to_create = await create_reaction(db, publication, reaction, user.id)
    return reaction_to_create


@router.delete("/{publication_id}/reaction")
async def delete_reaction(publication_id: PathID,
                          user: CurrentUser,
                          db: AsyncDBSession) -> ReactionRead:
    publication = await get_publication_by_id(db, publication_id)
    if not publication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    deleted_reaction = await delete_reaction_from_db(db, publication, user.id)
    if not deleted_reaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Reaction was not found")
    return deleted_reaction


@router.patch("/{publication_id}/reaction")
async def patch_reaction(publication_id: PathID,
                         reaction: ReactionCreate,
                         user: CurrentUser,
                         db: AsyncDBSession) -> ReactionRead:
    publication = await get_publication_by_id(db, publication_id)
    if not publication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    reaction_to_update = await get_user_reaction_to_publication(publication, user.id)
    if not reaction_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Reaction was not found")
    updated_reaction = await update_reaction(db, reaction_to_update, reaction)
    return updated_reaction
