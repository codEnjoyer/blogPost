from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


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
