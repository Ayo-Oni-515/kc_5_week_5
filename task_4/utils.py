import os


def does_note_exist(note_title: str) -> bool:
    """returns whether a note exists or not"""
    file_list = os.listdir()
    files_txt = []

    for file in file_list:
        if file.endswith(".txt"):
            file_name = file[0:-4]
            files_txt.append(file_name)

    return note_title in files_txt


def add_a_new_note(note_title: str, content: str):
    """creates a new note in the current directory"""
    if does_note_exist(note_title):
        raise NameError

    with open(f"{note_title}.txt", "w") as file:
        file.write(content)


def get_note(note_title: str):
    """get a note"""
    if not does_note_exist(note_title):
        raise NameError

    with open(f"{note_title}.txt", "r") as file:
        content = file.read()

    return content
