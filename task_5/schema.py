from pydantic import BaseModel


class ContactCreateModel(BaseModel):
    """create contact schema"""
    name: str
    phone: str
    email: str


class ContactCreateNameModel(BaseModel):
    """create contact schema"""
    phone: str
    email: str


class ContactResponseModel(BaseModel):
    """contact schema"""
    name: str
    phone: str
    email: str
