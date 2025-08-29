from fastapi import FastAPI, HTTPException, status

from schema import (ContactCreateModel,
                    ContactCreateNameModel,
                    ContactResponseModel)
from utils import add_contact, get_contact


# application's main entry point
app = FastAPI()


@app.post("/contacts/",
          status_code=status.HTTP_201_CREATED)
async def create_a_contact(contact_data: ContactCreateModel):
    """create a new contact endpoint"""
    try:
        add_contact(name=contact_data.name,
                    phone=contact_data.phone,
                    email=contact_data.email)
        return ContactResponseModel(
            name=contact_data.name,
            phone=contact_data.phone,
            email=contact_data.email
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Contact already exists!"
        )
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="Contact creation failed!"
        )


@app.get("/contacts/",
         status_code=status.HTTP_200_OK)
async def get_by_contact_name(name: str):
    """query parameter based endpoint for fetching a single contact"""
    try:
        contact_data: dict = get_contact(name)
        return ContactResponseModel(
            name=name,
            phone=contact_data["phone"],
            email=contact_data["email"]
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{name}'s data doesn't exist!"
        )


@app.post("/contacts/{name}",
          status_code=status.HTTP_201_CREATED)
async def create_a_contact_by_name(name: str,
                                   contact_data: ContactCreateNameModel):
    """returns all registered contacts"""
    try:
        add_contact(name=name,
                    phone=contact_data.phone,
                    email=contact_data.email)
        return ContactResponseModel(
            name=name,
            phone=contact_data.phone,
            email=contact_data.email
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Contact already exists!"
        )
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="Contact creation failed!"
        )
