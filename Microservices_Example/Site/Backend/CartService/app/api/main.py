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

@app.get("/api/carts", response_model=List[schemes.Cart])  # response_model показывает подсказку ожидаемого ответа от этого api (только pydantic схема)
async def get_carts():
    with SessionLocal() as session:
        carts = session.query(models.Cart).all()

    return carts

@app.get("/api/carts/{user_id}/get_products", response_model=List[schemes.CartProducts])
async def get_cart_products(user_id: int):
    with SessionLocal() as session:
        cart = session.query(models.Cart).filter_by(user_id=user_id).first()
        
        if (cart == None):
            raise HTTPException(status_code=404, detail=f'ERR: не удалось найти Cart для данного user_id={user_id}')

        cart_products = session.query(models.CartProduct).filter_by(cart_id=cart.id).all()
        
    return cart_products

@app.post("/api/carts/{user_id}/post_product/{product_id}")
async def post_cart_products(user_id: int, product_id: int):
    with SessionLocal() as session:
        cart = session.query(models.Cart).filter_by(user_id=user_id).first()
        
        if (cart == None):
            raise HTTPException(status_code=404, detail=f'ERR: не удалось найти Cart для данного user_id={user_id}')

        product = session.query(models.CartProduct).filter_by(cart_id=cart.id, product_id=product_id).first()
        
        # Увеличить количество
        if(product):
            product.quantity += 1
        else:
            product = models.CartProduct(cart_id=cart.id, product_id=product_id, quantity=1)
            session.add(product)
            
        # Запрос к калатогу товаров
        async with httpx.AsyncClient() as client:
            response = await client.get('http://localhost:8000/api/catalog')
        
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Error fetching data")
            
            # Расчитать цену
            data = json.loads(response.text)  # Преобразуем строку JSON в объект Python
            product.total = product.quantity * float(data[product_id - 1]['price'])
            
        if (product.total == None or product.total == 0):
            raise HTTPException(status_code=400, detail="Не удалось расчитать Total Price")
        
        session.commit()
        
    return {"msg": "response is success"}