from pydantic import BaseModel

from reactions.models import ReactionType


class ReactionBase(BaseModel):
    type: ReactionType


class ReactionRead(ReactionBase):
    publication_id: int
    author_id: int


class ReactionCreate(ReactionBase):
    pass
