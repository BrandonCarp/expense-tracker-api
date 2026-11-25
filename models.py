from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Relationship
from sqlalchemy import ForeignKey
from sqlalchemy import String
from typing import List
from typing import Optional
from datetime import date, datetime
# from typing import ClassVar

class Base(DeclarativeBase):
    pass
    created_at = datetime.now()


class User(Base):
    def __init__(self, id: int, email:str, hashed_password:str, created_at: datetime):
        __tablename__ = "users"


        self.id = id
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = created_at

