# contact class
class Contact():
    """contact class manages all contact-related data"""
    # In_memory: dict[str, dict] = {}

    def __init__(self,
                 name: str,
                 phone: str,
                 email: str):
        self.name = name
        self.phone = phone
        self.email = email

        # json serializable representation
        self.json = {
            self.name: {
                "phone": self.phone,
                "email": self.email
            }
        }

        # In memory storage
        # self.In_memory.update(**self.json)
