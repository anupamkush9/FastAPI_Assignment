from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(250))
    completed = Column(Boolean, default=False)


class TodoCreate(BaseModel):
    title: str
    description: str

class TodoRead(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
