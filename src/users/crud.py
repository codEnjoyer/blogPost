from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from users.models import User


async def get_all_users(db: AsyncSession, limit: int = 10, offset: int = 0) -> Sequence[User]:
    try:
        query = select(User).limit(limit).offset(offset)
        result = await db.execute(query)
        users = result.scalars().all()
        return users
    except Exception as e:
        raise e
