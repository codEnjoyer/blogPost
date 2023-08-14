from fastapi import HTTPException, status


class ReactionNotFoundException(HTTPException):
    def __init__(self, *, reaction_id: int = None):
        if not reaction_id:
            detail = "Reaction was not found"
        else:
            detail = f"Reaction with id {reaction_id} was not found"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=detail)
