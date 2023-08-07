from pydantic import BaseModel

from reactions.models import ReactionType


class Reaction(BaseModel):
    publication_id: int
    type: ReactionType
    author_id: int
