from sqlalchemy.orm import DeclarativeBase
from datetime import date, datetime
# from typing import ClassVar

class Base(DeclarativeBase):
    pass
    def __init__(self, created_at):
        self.created_at = datetime.now()


class Users(Base):
    def __init__(self, id: int, email:str, hashed_password:str, created_at: str):
        __tablename__ = "users"
        self.id = id
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = created_at

