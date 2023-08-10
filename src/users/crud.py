from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from publications.models import Publication
from reactions.models import Reaction
from users.models import User
from users.schemas import UserUpdate


async def get_all_users(db: AsyncSession, limit: int = 10, offset: int = 0) -> Sequence[User]:
    try:
        query = select(User).limit(limit).offset(offset)
        result = await db.execute(query)
        users = result.scalars().all()
        return users
    except Exception as e:
        raise e


async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
    try:
        query = select(User).filter(User.id == user_id)
        result = await db.execute(query)
        user = result.scalar()
        return user
    except Exception as e:
        raise e


async def update_user_by_id(db: AsyncSession,
                            user_id: int,
                            update_scheme: UserUpdate) -> User | None:
    try:
        db_user = await get_user_by_id(db, user_id)
        if not db_user:
            return None
        for field, value in update_scheme:
            if value:
                setattr(db_user, field, value)
        await db.commit()
        await db.refresh(db_user)
        return db_user
    except Exception as e:
        raise e


async def delete_user_by_id(db: AsyncSession, user_id: int) -> User:
    try:
        db_user = await get_user_by_id(db, user_id)
        await db.delete(db_user)
        await db.commit()
        return db_user
    except Exception as e:
        raise e


async def get_all_user_publications(db: AsyncSession,
                                    user_id: int,
                                    limit: int = 10,
                                    offset: int = 0) -> Sequence[Publication] | None:
    try:
        user = await get_user_by_id(db, user_id)
        if not user:
            return None
        query = select(Publication).filter(Publication.author_id == user_id).limit(limit).offset(offset)
        result = await db.execute(query)
        publications = result.scalars().all()
        return publications
    except Exception as e:
        raise e


async def get_all_user_reactions(db: AsyncSession,
                                 user_id: int,
                                 limit: int = 20,
                                 offset: int = 0) -> Sequence[Reaction] | None:
    try:
        user = await get_user_by_id(db, user_id)
        if not user:
            return None
        query = select(Reaction).filter(Reaction.author_id == user_id).limit(limit).offset(offset)
        result = await db.execute(query)
        reactions = result.scalars().all()
        return reactions
    except Exception as e:
        raise e
