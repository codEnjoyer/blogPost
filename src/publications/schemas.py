from datetime import datetime

from pydantic import BaseModel


class Publication(BaseModel):
    id: int
    author_id: int
    content: str
    published_at: datetime
    last_edit_at: datetime
