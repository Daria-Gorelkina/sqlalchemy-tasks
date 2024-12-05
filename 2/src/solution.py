import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Date, Float, Column, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])


# BEGIN (write your solution here)
class Base(DeclarativeBase):
    pass

# Определение модели Book
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256), unique=True, nullable=False)
    author = Column(String(128), nullable=False)
    published_date = Column(Date, nullable=True)
    pages = Column(Integer, nullable=True)
    genre = Column(String(64), nullable=True)
    rating = Column(Float, nullable=True)
# END

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
