from datetime import datetime

from pydantic import BaseModel


class PublicationBase(BaseModel):
    content: str


class PublicationRead(PublicationBase):
    id: int
    author_id: int
    published_at: datetime
    last_edit_at: datetime


class PublicationCreate(PublicationBase):
    pass


class PublicationUpdate(PublicationBase):
    content: str | None = None
