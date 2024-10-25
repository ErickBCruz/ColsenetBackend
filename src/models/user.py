from sqlalchemy import String, Column, Integer, Boolean, DateTime
from sqlalchemy.orm import declarative_base



Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)