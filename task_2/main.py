from fastapi import FastAPI


# application's main entry point
app = FastAPI()


@app.get("/products/")
async def get_all_products():
    """returns all available products"""


@app.post("/cart/add")
async def add_a_product(product_id, qty):
    """adds a product based on product id and quantity"""


@app.get("/cart/checkout")
async def cart_checkout():
    """checkout products added to cart"""
