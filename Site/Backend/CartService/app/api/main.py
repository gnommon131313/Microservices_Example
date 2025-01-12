import os
from typing import List
from fastapi import FastAPI, HTTPException, Depends
import httpx
import json
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware

from db import models
from db.engine import SessionLocal
from api import schemes


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" Разрешаем все источники, рекомендуется только для тестирования
    allow_credentials=True,
    allow_methods=["*"],  # "*" Разрешаем все методы
    allow_headers=["*"],  # "*" Разрешаем все заголовки
)

# Тестовая функция, т.к. нету регистации соостветсвенно карзине в БД неоткуда взяться
def test_create_user_cart(user_id: int) -> None:
    with SessionLocal() as session:
        cart = session.query(models.Cart).filter_by(user_id=user_id).first()

        if (cart):
            return
        
        cart_new = models.Cart(user_id=user_id)
        
        session.add(cart_new)
        session.commit()

@app.get("/api/carts/products/{user_id}", response_model=List[schemes.CartProducts])
async def read_cart_products(user_id: int):
    test_create_user_cart(user_id) # Плохой способ, но для тестов сойдет
    
    with SessionLocal() as session:
        cart = session.query(models.Cart).filter_by(user_id=user_id).first()
        
        if (cart == None):
            raise HTTPException(status_code=404, detail=f'ERR: не удалось найти Cart для данного user_id={user_id}')

        cart_products = session.query(models.CartProduct).filter_by(cart_id=cart.id).all()
        
    return cart_products

@app.post("/api/carts/products/{user_id}")
async def create_product_in_cart(user_id: int, cart_data: schemes.CartData):
    test_create_user_cart(user_id) # Плохой способ, но для тестов сойдет
    
    with SessionLocal() as session:
        cart = session.query(models.Cart).filter_by(user_id=user_id).first()
        
        if (cart == None):
            raise HTTPException(status_code=404, detail=f'ERR: не удалось найти Cart для данного user_id={user_id}')

        product = session.query(models.CartProduct).filter_by(cart_id=cart.id, product_id=cart_data.product_id).first()
        
        # Увеличить количество
        if(product):
            product.quantity += 1
        else:
            product = models.CartProduct(cart_id=cart.id, product_id=cart_data.product_id, quantity=1)
            session.add(product)
            
        # Запрос к калатогу товаров
        async with httpx.AsyncClient() as client:
            response = await client.get('http://localhost:8001/api/catalog/products')
        
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Error fetching data")
            
            # Расчитать цену
            data = json.loads(response.text)  # Преобразуем строку JSON в объект Python
            product.total = product.quantity * float(data[product.product_id - 1]['price'])
            
        if (product.total == None or product.total == 0):
            raise HTTPException(status_code=400, detail="Не удалось расчитать Total Price")
        
        session.commit()
        
    return {"msg": "response is success"}