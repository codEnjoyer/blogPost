from fastapi import HTTPException, status


class PublicationNotFound(HTTPException):
    def __init__(self, *, publication_id: int):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"Publication with id {publication_id} was not found")


class NotAuthorOfPublicationException(HTTPException):
    def __init__(self, *, publication_id: int):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN,
                         detail=f"You are not the author of publication with id {publication_id}")


class SelfReactionException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST,
                         detail="You can't react to your own publication")
