from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from publications.models import Publication

from reactions.models import Reaction, ReactionType
from reactions.schemas import ReactionCreate


async def get_all_reactions(publication: Publication,
                            limit: int = 20,
                            offset: int = 0) -> Sequence[Reaction] | None:
    try:
        reactions = publication.reactions[offset:offset + limit]
        return reactions
    except Exception as e:
        raise e


async def get_user_reaction(publication: Publication,
                            user_id: int) -> Reaction | None:
    try:
        user_reactions = (r for r in publication.reactions if r.author_id == user_id)
        user_reaction = next(user_reactions, None)
        return user_reaction
    except Exception as e:
        raise e


async def get_user_reaction_to_publication(publication: Publication,
                                           user_id: int) -> Reaction:
    try:
        default_reaction = Reaction(author_id=user_id, type=ReactionType.none, publication_id=publication.id)
        user_reaction = await get_user_reaction(publication, user_id)
        if not user_reaction:
            user_reaction = default_reaction
        return user_reaction
    except Exception as e:
        raise e


async def create_reaction(db: AsyncSession,
                          publication: Publication,
                          reaction: ReactionCreate,
                          user_id: int) -> Reaction | None:
    try:
        existing_reaction = await get_user_reaction(publication, user_id)
        if existing_reaction:
            updated_reaction = await update_reaction(db, existing_reaction, reaction)
            return updated_reaction
        else:
            reaction_to_create = Reaction(**reaction.model_dump(), author_id=user_id)
            publication.reactions.append(reaction_to_create)
            await db.commit()
            await db.refresh(reaction_to_create)
            return reaction_to_create
    except Exception as e:
        await db.rollback()
        raise e


async def delete_reaction_from_db(db: AsyncSession,
                                  publication: Publication,
                                  user_id: int) -> Reaction | None:
    try:
        existing_reaction = await get_user_reaction(publication, user_id)
        if not existing_reaction:
            return None
        publication.reactions.remove(existing_reaction)
        await db.commit()
        return existing_reaction
    except Exception as e:
        await db.rollback()
        raise e


async def update_reaction(db: AsyncSession,
                          existing_reaction: Reaction,
                          reaction: ReactionCreate) -> Reaction:
    try:
        existing_reaction.type = reaction.type
        await db.commit()
        await db.refresh(existing_reaction)
        return existing_reaction
    except Exception as e:
        await db.rollback()
        raise e
