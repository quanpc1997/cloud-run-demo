from fastapi import FastAPI
from faker import Faker
from pydantic import BaseModel
from typing import List
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()
fake = Faker()

# Read configuration from environment variables
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.environ["PORT"])
DEFAULT_LIMIT = int(os.getenv("DEFAULT_LIMIT", 5))

class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str

class Order(BaseModel):
    id: int
    user_name: str
    product_name: str
    quantity: int

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/users", response_model=List[User])
def get_users(limit: int = DEFAULT_LIMIT):
    return [
        User(id=i, name=fake.name(), email=fake.email(), phone=fake.phone_number())
        for i in range(1, limit + 1)
    ]

@app.get("/products", response_model=List[Product])
def get_products(limit: int = DEFAULT_LIMIT):
    return [
        Product(id=i, name=fake.word(), price=float(fake.random_int(10, 1000)), description=fake.text())
        for i in range(1, limit + 1)
    ]

@app.get("/orders", response_model=List[Order])
def get_orders(limit: int = DEFAULT_LIMIT):
    return [
        Order(id=i, user_name=fake.name(), product_name=fake.word(), quantity=fake.random_int(1, 10))
        for i in range(1, limit + 1)
    ]

@app.get("/addresses", response_model=List[dict])
def get_addresses(limit: int = DEFAULT_LIMIT):
    return [
        {"id": i, "address": fake.address(), "city": fake.city(), "country": fake.country()}
        for i in range(1, limit + 1)
    ]

@app.get("/companies", response_model=List[dict])
def get_companies(limit: int = DEFAULT_LIMIT):
    return [
        {"id": i, "name": fake.company(), "industry": fake.word(), "website": fake.url()}
        for i in range(1, limit + 1)
    ]

@app.get("/config")
def get_config():
    return {
        "host": HOST,
        "port": PORT,
        "default_limit": DEFAULT_LIMIT,
        "environment": os.getenv("ENVIRONMENT", "development"),
        "log_level": os.getenv("LOG_LEVEL", "INFO")
    }

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)