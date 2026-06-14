from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class Login(BaseModel):
    email:str
    password:str

class CarCreate(BaseModel):
    car_name:str
    model:str
    price_per_day:int
    status:str

class BookingCreate(BaseModel):
    user_id:int
    car_id:int
    booking_date:date
    return_date:date
    status:str