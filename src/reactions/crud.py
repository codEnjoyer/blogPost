from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from publications.crud import get_publication_by_id
from publications.models import Publication

from reactions.models import Reaction, ReactionType


async def get_all_reactions(publication: Publication,
                            limit: int = 20,
                            offset: int = 0) -> Sequence[Reaction] | None:
    try:
        reactions = publication.reactions[offset:offset + limit]
        return reactions
    except Exception as e:
        raise e


async def get_user_reaction_to_publication(publication: Publication,
                                           user_id: int) -> Reaction:
    try:
        default_reaction = Reaction(author_id=user_id, type=ReactionType.none, publication_id=publication.id)
        user_reactions = (r for r in publication.reactions if r.author_id == user_id)
        user_reaction = next(user_reactions, default_reaction)
        return user_reaction
    except Exception as e:
        raise e
