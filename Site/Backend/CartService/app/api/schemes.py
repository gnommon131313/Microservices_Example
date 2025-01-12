from pydantic import BaseModel, Field


class Cart(BaseModel):
    id: int
    user_id: int  # при необходимости само расширеться до BigInteger, в отличии от моделей sqlalchemy
    
    
class CartProducts(BaseModel):
    cart_id: int
    product_id: int
    quantity: int
    total: int
    
class CartData(BaseModel):
    product_id : int = Field(alias='productId') # важно, чтобы названия полей в JSON запросе совпадали с названиями атрибутов в pydantic модели. Можно просто назвать поля и атрибуты одинаково, но т.к. в JS и Python приняты разные именования полей тут это будет не сооответствовать стандарту и лучше использовать связывание с полем через `int = Field(alias='НАЗЫВАНИЕ ПОЛЮ В JSON ЗАПРОСЕ')` 