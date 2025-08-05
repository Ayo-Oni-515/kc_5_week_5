import os
import json

from job_application import JobApplication
from schema import AllApplicationsModel, CreateApplicationModel


def is_json_file(file_path: str = "./applications.json") -> bool:
    """checks if json file exists"""
    return os.path.exists(file_path)


def save_to_json(
        data_to_save, file_path: str = "./applications.json") -> None:
    """saves data to a json file"""
    existing_data = load_from_json(file_path)
    existing_data.update(data_to_save)

    # handle
    with open(file_path, "w") as data_file:
        json.dump(existing_data, data_file, indent=4)


def load_from_json(file_path: str = "./applications.json") -> dict:
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


def does_application_record_exist(
        applicant_name: str,
        file_path: str = "./applications.json") -> bool:
    """return whether an applicant exists or not"""
    stored_data: dict = load_from_json(file_path)

    if applicant_name in stored_data.keys():
        return True

    return False


def create_an_application(applicant_data: CreateApplicationModel):
    """creates a new application record"""

    if does_application_record_exist(applicant_data.name):
        # raise an error if the applicant's data exists.
        raise KeyError
    else:
        # creates a new application in application.json
        data = applicant_data.model_dump()
        new_application: JobApplication = JobApplication(
            name=data["name"],
            company=data["company"],
            position=data["position"],
            status=data["status"]
        )
        save_to_json(new_application.json)

        return data


def get_all_applications(file_path: str = "./applications.json"):
    """returns all saved application records"""
    all_applications: AllApplicationsModel = AllApplicationsModel(
        data=load_from_json(file_path))
    return all_applications


def get_application_by_status(
        application_status: str, file_path: str = "./applications.json"):
    """returns all application record by status"""
    output: dict = {}
    stored_data: dict = load_from_json(file_path)

    for name in stored_data:
        if stored_data[name]["status"] == application_status:
            output.update(stored_data[name])
        else:
            continue

    return AllApplicationsModel(data=output)
