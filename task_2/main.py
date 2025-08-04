from fastapi import FastAPI, status, HTTPException

from cart import get_all_products, get_checkout, add_product_to_cart
from schema import AllProductModel, AllCartModel, AddToCartModel


# application's main entry point
app = FastAPI()


@app.get("/products/",
         status_code=status.HTTP_200_OK,
         response_model=AllProductModel)
async def get_products():
    """returns all available products"""
    try:
        return get_all_products()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Couldn't process request!"
        )


@app.post("/cart/add",
          status_code=status.HTTP_200_OK,
          response_model=AddToCartModel)
async def add_to_cart(product_id: str, qty: int):
    """adds a product based on product id and quantity"""
    try:
        add_product_to_cart(product_id, qty)
        return AddToCartModel(product_id=product_id, qty=qty)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product isn't in inventory"
        )
    except NameError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product exists in cart already!"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="'Add to cart opertion' failed!"
        )


@app.get("/cart/checkout",
         status_code=status.HTTP_200_OK,
         response_model=AllCartModel)
async def cart_checkout():
    """checkout products added to cart"""
    try:
        return get_checkout()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Couldn't process request!"
        )
