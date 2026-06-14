from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    car_name = Column(String)
    model = Column(String)
    price_per_day = Column(Integer)
    status = Column(String)

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    car_id = Column(Integer)
    booking_date = Column(Date)
    return_date = Column(Date)
    status = Column(String)