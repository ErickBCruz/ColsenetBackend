from sqlalchemy import String, Column, Integer, Boolean, DateTime
from sqlalchemy.orm import declarative_base



Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    details = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)