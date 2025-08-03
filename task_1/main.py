from fastapi import FastAPI, HTTPException, status

from schema import StudentCreateModel, StudentModel, AllStudentModel
from utils import add_student, get_student, get_all_students  # noqa


# application's main entry point
app = FastAPI()


@app.post("/students/",
          status_code=status.HTTP_201_CREATED)
async def create_a_student(student_data: StudentCreateModel):
    """create a student endpoint"""
    student = student_data.model_dump()

    student_name: str = student["name"]
    student_subjects: dict = student["subjects"]

    try:
        new_student_data = add_student(student_name, student_subjects)
        return new_student_data
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student data already exists!"
        )
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="Student data creation failed!"
        )


@app.get("/students/{name}")
async def get_by_student_name(name: str):
    """path parameter based endpoint for fetching a single student"""


@app.get("/students/",
         status_code=status.HTTP_200_OK,
         response_model=AllStudentModel)
async def get_students():
    """returns all registered students"""
    try:
        return get_all_students()
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="Error retrieving data!"
        )
