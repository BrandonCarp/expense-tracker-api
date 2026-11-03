import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set — copy .env.example to .env and fill it in")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)