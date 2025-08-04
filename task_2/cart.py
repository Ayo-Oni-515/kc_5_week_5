import json
import os

from products import Product
from schema import AllProductModel, AllCartModel, ProductModel


def is_json_file(file_path: str = "./cart.json") -> bool:
    """checks if json file exists"""
    return os.path.exists(file_path)


def save_to_json(
        data_to_save, file_path: str = "./cart.json") -> None:
    """saves data to a json file"""
    existing_data = load_from_json(file_path)
    existing_data.update(data_to_save)

    # handle
    with open(file_path, "w") as data_file:
        json.dump(existing_data, data_file, indent=4)


def load_from_json(file_path: str = "./cart.json") -> dict:
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


def does_product_exist(product_id: str) -> bool:
    """returns whether a product exists or not"""
    if product_id in Product.In_memory.keys():
        return True

    return False


def is_product_in_cart(product_id: str, file_path: str = "./cart.json"):
    """checks if product has been added to cart already"""
    cart: dict = load_from_json(file_path)

    if product_id in cart:
        return True

    return False


def get_all_products():
    """returns all available products"""
    try:
        return AllProductModel(data=Product.In_memory)
    except Exception:
        raise


def get_checkout(file_path: str = "./cart.json"):
    """returns all products added to cart"""
    try:
        return AllCartModel(data=load_from_json(file_path))
    except Exception:
        raise


def add_product_to_cart(
        product_id: str, product_qty: int, file_path: str = "./cart.json"):
    """adds a product to cart"""
    if does_product_exist(product_id):
        if not is_product_in_cart(product_id):
            """add product to cart"""
            new_product = ProductModel(
                name=Product.In_memory[product_id]["name"],
                price=Product.In_memory[product_id]["price"],
                qty=product_qty
            ).model_dump()
            product = {product_id: new_product}
            save_to_json(product)
            return product
        elif is_product_in_cart(product_id):
            # product already in cart
            """return 'product exists in cart'"""
            raise NameError

    else:
        # product doesn't exist in inventory
        raise KeyError
