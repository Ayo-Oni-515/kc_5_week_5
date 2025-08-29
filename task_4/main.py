from fastapi import FastAPI, HTTPException, status
from utils import add_a_new_note, get_note
from schema import NoteCreateModel, NoteCreatePathModel, NoteResponseModel


# application's main entry point
app = FastAPI()


@app.post("/notes/",
          status_code=status.HTTP_201_CREATED)
async def create_a_note(note_data: NoteCreateModel):
    """creates a new note"""
    try:
        add_a_new_note(note_data.title, note_data.content)
        return NoteResponseModel(title=note_data.title,
                                 content=note_data.content)
    except NameError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"{note_data.title} note already exist")
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Note creation failed!")


@app.get("/notes/{title}",
         status_code=status.HTTP_200_OK)
async def get_a_note_by_title(title: str):
    """returns a note by title"""
    try:
        output: str = get_note(title)
        return NoteResponseModel(title=title,
                                 content=output)
    except NameError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Note doesn't exist")


@app.post("/notes/{title}",
          status_code=status.HTTP_201_CREATED)
async def create_a_note_by_title(title: str, note_data: NoteCreatePathModel):
    """create a new note by title (with path parameter)"""
    try:
        add_a_new_note(title, note_data.content)
        return NoteResponseModel(title=title,
                                 content=note_data.content)
    except NameError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"{title} note already exist")
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Note creation failed!")
