from contact import Contact


contact_store: dict = {}


def does_contact_exist(contact_name: str) -> bool:
    """returns whether contat record exists or not"""
    return contact_name in contact_store.keys()


def add_contact(name, phone, email):
    """adds a contact record to contact"""
    if does_contact_exist(name):
        # raise an error if the contact's data exists.
        raise KeyError
    else:
        # creates a new contact data in dict
        new_contact: Contact = Contact(name, phone, email)
        contact_store.update(**new_contact.json)


def get_contact(name: str):
    """returns a contact based on name provided"""
    if does_contact_exist(name):
        # return contact details
        all_contacts: dict = contact_store
        return all_contacts[name]

    raise KeyError
