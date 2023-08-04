from typing import Annotated

from fastapi import APIRouter, Depends

from auth.base_config import current_user
from users.models import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/protected_route")
async def protected_route(user: Annotated[User, Depends(current_user)]):
    return f"This is a protected route, {user.username}"


@router.get("/")
async def get_users():
    pass


@router.get("/{user_id}")
async def get_user(user_id: int):
    pass


@router.get("/{user_id}/publications")
async def get_user_publications(user_id: int):
    pass


@router.get("/{user_id}/reactions")
async def get_user_reactions(user_id: int):
    pass
