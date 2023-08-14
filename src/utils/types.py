from typing import Annotated

from fastapi import Depends, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from database import get_async_session
from users.models import User

PathID = Annotated[int, Path(gt=0, lt=2 ** 31)]
CurrentUser = Annotated[User, Depends(current_user)]

AsyncDBSession = Annotated[AsyncSession, Depends(get_async_session)]
QueryDBLimit = Annotated[int, Query(ge=0, le=10 ** 3)]
QueryDBOffset = Annotated[int, Query(ge=0, le=10 ** 6)]
