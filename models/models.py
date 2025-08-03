from sqlalchemy import Column, Integer, String
from db.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(255))

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(100),unique=True)
    phone = Column(Integer)