from fastapi import APIRouter, Depends

from auth.base_config import current_user

router = APIRouter(prefix="/reactions", tags=["Reactions"])


@router.get("/{publication_id}")
async def get_publication_reactions(publication_id: int):
    pass


@router.post("/{publication_id}")
async def create_publication_reaction(publication_id: int, user=Depends(current_user)):
    pass
