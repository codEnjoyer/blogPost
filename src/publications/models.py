from datetime import datetime

from sqlalchemy import DateTime, func, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Publication(Base):
    __tablename__ = "publication"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False, default="Hello, World!")
    published_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    last_edit_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    author: Mapped["User"] = relationship(back_populates="publications")
    reactions: Mapped[list["Reaction"]] = relationship(back_populates="publication", cascade="all, delete-orphan",
                                                       lazy="subquery")
