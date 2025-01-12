import os
from typing import List
from fastapi import FastAPI, HTTPException, Depends
import httpx
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware

from db import models
from db.engine import SessionLocal


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" Разрешаем все источники, рекомендуеться только для тестирования
    allow_credentials=True,
    allow_methods=["*"],  # "*" Разрешаем все методы
    allow_headers=["*"],  # "*" Разрешаем все заголовки
)

@app.get("/api/catalog/products")
async def get_products():
    with SessionLocal() as session:
        products = session.query(models.Product).all()
    
    return products