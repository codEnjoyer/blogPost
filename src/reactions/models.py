from enum import StrEnum

from sqlalchemy import Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class ReactionType(StrEnum):
    like: str = "like"
    dislike: str = "dislike"


class Reaction(Base):
    __tablename__ = "reaction"

    publication_id: Mapped[int] = mapped_column(Integer, ForeignKey("publication.id"), nullable=False, primary_key=True)
    type: Mapped[ReactionType] = mapped_column(Enum(ReactionType), nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False, primary_key=True)

    author: Mapped["User"] = relationship(back_populates="reactions")
    publication: Mapped["Publication"] = relationship(back_populates="reactions")
