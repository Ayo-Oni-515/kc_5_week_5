from pydantic import BaseModel


class ProductModel(BaseModel):
    name: str
    price: float
    qty: int
    amount: float


class AllProductModel(BaseModel):
    data: dict


class AllCartModel(BaseModel):
    data: dict


class AddToCartModel(BaseModel):
    product_id: str
    qty: int
