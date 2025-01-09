from pydantic import BaseModel, Field


class Cart(BaseModel):
    id: int
    user_id: int  # при необходимости само расширеться до BigInteger, в отличии от моделей sqlalchemy
    
    
class CartProducts(BaseModel):
    cart_id: int
    product_id: int
    quantity: int
    total: int