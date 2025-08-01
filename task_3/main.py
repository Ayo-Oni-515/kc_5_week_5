from fastapi import FastAPI


# application's main entry point
app = FastAPI()


@app.post("/applications/")
async def create_an_application():
    """creates a new application"""


@app.get("/applications/")
async def get_all_applications():
    """returns all applications"""


@app.get("/applications/search")
async def search_applications_by_status():
    """returns all applications matching a given status"""
