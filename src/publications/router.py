from fastapi import APIRouter, Depends

from auth.base_config import current_user

router = APIRouter(prefix="/publications", tags=["Publications"])


@router.get("/")
async def get_publications():
    pass


@router.post("/")
async def create_publication(user=Depends(current_user)):
    pass


@router.delete("/{publication_id}")
async def delete_publication(publication_id: int, user=Depends(current_user)):
    pass


@router.put("/{publication_id}")
async def put_publication(publication_id: int, user=Depends(current_user)):
    pass


@router.patch("/{publication_id}")
async def patch_publication(publication_id: int, user=Depends(current_user)):
    pass
