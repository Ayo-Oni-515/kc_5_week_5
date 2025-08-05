# job application class

class JobApplication:
    def __init__(self, name, company, position, status):
        self.name = name
        self.company = company
        self.position = position
        self.status = status

        # json serializable representation
        self.json = {
            self.name: {
                "company": self.company,
                "position": self.position,
                "status": self.status
            }
        }
