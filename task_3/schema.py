from typing import Literal
from pydantic import BaseModel


class CreateApplicationModel(BaseModel):
    name: str
    company: str
    position: str
    status: Literal["open", "closed", "pending"]


class AllApplicationsModel(BaseModel):
    data: dict
