from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from database import get_async_session
from publications.crud import get_all_publications, get_publication_by_id, create_publication
from publications.schemas import PublicationRead, PublicationCreate, PublicationUpdate
from users.models import User

router = APIRouter(prefix="/publications", tags=["Publications"])


@router.get("/")
async def get_publications(db: Annotated[AsyncSession, Depends(get_async_session)],
                           limit: int = 20,
                           offset: int = 0) -> list[PublicationRead]:
    publications = await get_all_publications(db, limit, offset)
    return list(publications)


@router.get("/{publication_id}")
async def get_publication(db: Annotated[AsyncSession, Depends(get_async_session)],
                          publication_id: int) -> PublicationRead | None:
    publication = await get_publication_by_id(db, publication_id)
    if not publication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Publication was not found")
    return publication


@router.post("/")
async def post_publication(user: Annotated[User, Depends(current_user)],
                           db: Annotated[AsyncSession, Depends(get_async_session)],
                           publication: PublicationCreate) -> PublicationRead:
    created_publication = await create_publication(db, publication, user.id)
    return created_publication


@router.delete("/{publication_id}")
async def delete_publication(publication_id: int, user=Depends(current_user)):
    pass


@router.put("/{publication_id}")
async def put_publication(publication_id: int, user=Depends(current_user)):
    pass


@router.patch("/{publication_id}")
async def patch_publication(publication_id: int, user=Depends(current_user)):
    pass
