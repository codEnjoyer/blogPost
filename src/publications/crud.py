from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from publications.models import Publication
from publications.schemas import PublicationCreate


async def get_all_publications(db: AsyncSession,
                               limit: int = 20,
                               offset: int = 0) -> Sequence[Publication]:
    try:
        query = select(Publication).limit(limit).offset(offset)
        result = await db.execute(query)
        publications = result.scalars().all()
        return publications
    except Exception as e:
        raise e


async def get_publication_by_id(db: AsyncSession, id: int) -> Publication | None:
    try:
        query = select(Publication).filter(Publication.id == id)
        result = await db.execute(query)
        publication = result.scalar()
        return publication
    except Exception as e:
        raise e


async def create_publication(db: AsyncSession,
                             publication: PublicationCreate,
                             author_id: int) -> Publication:
    try:
        db_item = Publication(**publication.model_dump(), author_id=author_id)
        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        return db_item
    except Exception as e:
        await db.rollback()
        raise e


async def delete_publication_from_db(db: AsyncSession,
                                     publication: Publication) -> Publication:
    try:
        await db.delete(publication)
        await db.commit()
        return publication
    except Exception as e:
        await db.rollback()
        raise e
