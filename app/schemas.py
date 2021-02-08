from typing import List, Optional

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    text: Optional[str] = None


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    email: str
    password: str


class User(UserBase):
    id: int
    email: str
    is_active: bool
    Notes: List[Note] = []

    class Config:
        orm_mode = True
