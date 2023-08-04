from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from pydantic import EmailStr
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from publications.models import Publication, Reaction


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[EmailStr] = mapped_column(String, nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    publications: Mapped[list[Publication]] = relationship(back_populates="author")
    reactions: Mapped[list[Reaction]] = relationship(back_populates="author")
