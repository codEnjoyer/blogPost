from fastapi import HTTPException, status


class ReactionNotFound(HTTPException):
    def __init__(self, *, reaction_id: int):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"Reaction with id {reaction_id} was not found")
