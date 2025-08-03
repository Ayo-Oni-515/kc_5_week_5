from pydantic import BaseModel


class StudentCreateModel(BaseModel):
    """create student schema"""
    name: str
    subjects: dict[str, float]


class StudentModel(BaseModel):
    """create student schema"""
    name: str
    subjects: dict[str, float]
    average: float
    grade: str


class AllStudentModel(BaseModel):
    data: dict[str, dict]
