import os
from typing import List
from fastapi import FastAPI, HTTPException, Depends
import httpx
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware
import re


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

# Симулиция получения адресов сервисов через Server Discovery
USER_SERVICE_URL = "http://localhost:8003/api/users"
CATALOG_SERVICE_URL = "http://localhost:8001/api/catalog"
CART_SERVICE_URL = "http://localhost:8002/api/carts"

# Функция с помощью которой другие http запросы будут перенаправлены на нужный адресс
async def fetch_service(request: str, url: str) -> dict:
    async with httpx.AsyncClient() as client:
        if (request == "get"):
            response = await client.get(url)
        elif (request == "post"):
            response = await client.post(url)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching data")
        
        return response.json()

@app.get("/api/users")
async def get_users():
    response = await fetch_service("get", USER_SERVICE_URL)
    return response

@app.get("/api/catalog")
async def get_catalog():
    response = await fetch_service("get", CATALOG_SERVICE_URL)
    return response

@app.get("/api/carts")
async def get_carts():
    response = await fetch_service("get", CART_SERVICE_URL)
    return response

@app.get("/api/carts/{user_id}/get_products")
async def get_cart_products(user_id: int):
    response = await fetch_service("get", f"{CART_SERVICE_URL}/{user_id}/get_products")
    return response