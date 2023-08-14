from fastapi import HTTPException, status


class PublicationNotFound(HTTPException):
    def __init__(self, *, reaction_id: int):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"Publication with id {reaction_id} was not found")
