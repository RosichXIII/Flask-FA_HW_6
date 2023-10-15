from pydantic import BaseModel, Field
from datetime import datetime, date

class User(BaseModel):
    id: int = Field(default=None)
    name: str = Field(min_length=2, max_length=50)
    surname: str = Field(min_length=2, max_length=50)
    email: str = Field(min_length=4, max_length=50)
    password: str = Field(min_length=5, max_length=120)

class UserIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    surname: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., min_length=4, max_length=50)
    password: str = Field(..., min_length=5, max_length=120)

class Goods(BaseModel):
    id: int = Field(default=None)
    name: str = Field(min_length=2, max_length=50)
    description: str = Field(min_length=2, max_length=200)
    price: float = Field(..., ge=0.1, le=100000)

class GoodsIn(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    description: str = Field(min_length=2, max_length=200)
    price: float = Field(..., ge=0.1, le=100000)

class Order(BaseModel):
    id: int = Field(default=None)
    order_date: date = Field(default=datetime.now())
    status: str = Field(default='in_progress')
    user_id: int
    goods_id: int

class OrderIn(BaseModel):
    order_date: date = Field(default=datetime.now())
    status: str = Field(default='in_progress')
    user_id: int
    goods_id: int