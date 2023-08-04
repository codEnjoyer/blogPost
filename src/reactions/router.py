from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user

router = APIRouter(prefix="/reactions", tags=["Reactions"])


@router.get("/{publication_id}/reaction")
async def get_publication_reactions(publication_id: int):
    pass


@router.post("/{publication_id}/reaction")
async def create_publication_reaction(publication_id: int, user=Depends(get_current_user)):
    pass
