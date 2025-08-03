import os
import json

from student import Student
from schema import StudentModel, AllStudentModel


def is_json_file(file_path: str = "./students.json") -> bool:
    """checks if json file exists"""
    return os.path.exists(file_path)


def save_to_json(
        data_to_save, file_path: str = "./students.json") -> None:
    """saves data to a json file"""
    existing_data = load_from_json(file_path)
    existing_data.update(data_to_save)

    # handle
    with open(file_path, "w") as data_file:
        json.dump(existing_data, data_file, indent=4)


def load_from_json(file_path: str = "./students.json") -> dict:
    """loads data from a json file"""
    retrieved_data: list = {}

    if is_json_file(file_path):
        with open(file_path, "r") as data_file:
            # read from an existing json file

            try:
                # handle
                # parse existing data in json file
                retrieved_data = json.load(data_file)
            except Exception:
                # returns an empty dictionary if file is empty
                retrieved_data = {}

    else:
        # handle
        with open(file_path, "w") as data_file:
            save_to_json({}, file_path)

    return retrieved_data


def does_student_exist(
        student_name: str, file_path: str = "./students.json") -> bool:
    """returns whether student record exists or not"""
    stored_data: dict = load_from_json(file_path)

    if student_name in stored_data.keys():
        return True

    return False


def add_student(student_name: str, student_subjects: dict[str, float]):
    """adds a student record to students.json"""

    if does_student_exist(student_name):
        # raise an error if the student's data exists.
        raise KeyError
    else:
        # creates a new student data in students.json
        new_student: Student = Student(student_name, student_subjects)
        save_to_json(new_student.json)

        return new_student.json


def get_student(student_name: str, file_path: str = "./students.json"):
    """returns a student based on name provided"""
    if does_student_exist(student_name):
        # return student details
        all_students: dict = load_from_json(file_path)
        student_data = StudentModel(
            name=student_name,
            subjects=all_students[student_name]["subjects"],
            average=all_students[student_name]["average"],
            grade=all_students[student_name]["grade"]
        )
        return student_data.model_dump()

    raise KeyError


def get_all_students(file_path: str = "./students.json"):
    """returns all students in students.json"""
    all_students: AllStudentModel = AllStudentModel(
        data=load_from_json(file_path))
    return all_students
