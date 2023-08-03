from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from config import DB_URL

metadata = MetaData()
Base = declarative_base(metadata=metadata)

engine = create_engine(DB_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)


async def get_session() -> Session:
    with session_maker() as session:
        yield session
