from fastapi import APIRouter, HTTPException, status

from publications.crud import (
    get_all_publications, get_publication_by_id, create_publication,
    delete_publication_from_db, update_publication)
from publications.schemas import PublicationRead, PublicationCreate, PublicationUpdate
from utils.types import AsyncDBSession, QueryDBLimit, QueryDBOffset, PathID, CurrentUser

router = APIRouter(prefix="/publications", tags=["Publications"])


@router.get("/")
async def get_publications(db: AsyncDBSession,
                           limit: QueryDBLimit = 20,
                           offset: QueryDBOffset = 0) -> list[PublicationRead]:
    publications = await get_all_publications(db, limit, offset)
    return list(publications)


@router.get("/{publication_id}")
async def get_publication(publication_id: PathID,
                          db: AsyncDBSession) -> PublicationRead | None:
    publication = await get_publication_by_id(db, publication_id)
    if not publication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    return publication


@router.post("/")
async def post_publication(publication: PublicationCreate,
                           user: CurrentUser,
                           db: AsyncDBSession) -> PublicationRead:
    created_publication = await create_publication(db, publication, user.id)
    return created_publication


@router.delete("/{publication_id}")
async def delete_publication(publication_id: PathID,
                             user: CurrentUser,
                             db: AsyncDBSession) -> PublicationRead:
    publication_to_delete = await get_publication_by_id(db, publication_id)
    if not publication_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    if publication_to_delete.author_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You are not the author of this publication")
    deleted_publication = await delete_publication_from_db(db, publication_to_delete)
    return deleted_publication


@router.patch("/{publication_id}")
async def edit_publication(publication_id: PathID,
                           publication: PublicationUpdate,
                           user: CurrentUser,
                           db: AsyncDBSession) -> PublicationRead:
    publication_to_edit = await get_publication_by_id(db, publication_id)
    if not publication_to_edit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    if publication_to_edit.author_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You are not the author of this publication")
    edited_publication = await update_publication(db, publication_to_edit, publication)
    return edited_publication
