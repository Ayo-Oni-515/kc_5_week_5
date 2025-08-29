from typing import Optional
from pydantic import BaseModel


class NoteCreateModel(BaseModel):
    title: str
    content: Optional[str] = None


class NoteCreatePathModel(BaseModel):
    content: Optional[str] = None


class NoteResponseModel(BaseModel):
    title: str
    content: str
