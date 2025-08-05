from fastapi import FastAPI, status, HTTPException
from schema import CreateApplicationModel, AllApplicationsModel

from file_handler import (create_an_application,
                          get_all_applications,
                          get_application_by_status)


# application's main entry point
app = FastAPI()


@app.post("/applications/",
          status_code=status.HTTP_200_OK,
          response_model=CreateApplicationModel)
async def create_application(applicant_data: CreateApplicationModel):
    """creates a new application"""
    try:
        return create_an_application(applicant_data)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Application record already exists!"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application creation failed!"
        )


@app.get("/applications/",
         status_code=status.HTTP_200_OK)
async def get_applications():
    """returns all applications"""
    try:
        return get_all_applications()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error retrieving applications"
        )


@app.get("/applications/search",
         status_code=status.HTTP_200_OK,
         response_model=AllApplicationsModel)
async def search_applications_by_status(application_status: str):
    """returns all applications matching a given status"""
    try:
        return get_application_by_status(application_status)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Couldn't process request!"
        )
