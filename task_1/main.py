from fastapi import FastAPI


# application's main entry point
app = FastAPI()


@app.post("/students/")
async def create_a_student():
    """create a student endpoint"""


@app.get("/students/{name}")
async def get_by_student_name(name: str):
    """path parameter based endpoint for fetching a single student"""


@app.get("/students/")
async def get_all_students():
    """returns all registered students"""
