# product class
class Product:
    In_memory: dict = {}

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

        self.json = {
            self.id: {
                "name": self.name,
                "price": self.price
            }
        }

        # In memory storage
        self.In_memory.update(**self.json)


# dummy data
Product('p001', 'eggs', 70)
Product('p002', 'milk', 80)
Product('p003', 'butter', 30.5)
Product('p004', 'cereal', 15)
Product('p005', 'noodles', 66)
Product('p006', 'spaghetti', 25)
Product('p007', 'oil', 99)
Product('p008', 'macaroni', 50.3)
Product('p009', 'cheese', 22.24)
Product('p010', 'pepper', 40.65)
