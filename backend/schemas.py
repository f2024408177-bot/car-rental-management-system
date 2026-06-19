from pydantic import BaseModel
from datetime import date


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class CarCreate(BaseModel):
    car_name: str
    model: str
    price_per_day: int
    status: str


class BookingCreate(BaseModel):
    user_id: int
    car_id: int
    booking_date: date
    return_date: date

class CarUpdate(BaseModel):
    car_name: str
    model: str
    price_per_day: int
    status: str