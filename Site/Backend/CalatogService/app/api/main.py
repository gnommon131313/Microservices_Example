import os, re
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
    allow_origins=[
        "http://localhost",
        "http://127.0.0.1",
        "http://localhost:*",
        "http://127.0.0.1:*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/catalog/products")
async def get_products():
    with SessionLocal() as session:
        products = session.query(models.Product).all()
    
    return products