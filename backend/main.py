from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, User, Car, Booking
from schemas import UserCreate, UserLogin, CarCreate, BookingCreate

app = FastAPI(title="Car Rental Management System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Car Rental Management System API Running"}


# REGISTER USER
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User Registered Successfully"}


# LOGIN USER
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.email == user.email,
        User.password == user.password
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    return {"message": "Login Successful"}

# VIEW ALL CARS
@app.get("/cars")
def get_cars(db: Session = Depends(get_db)):
    return db.query(Car).all()


# VIEW SINGLE CAR
@app.get("/cars/{car_id}")
def get_car(car_id: int, db: Session = Depends(get_db)):

    car = db.query(Car).filter(
        Car.id == car_id
    ).first()

    if not car:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    return car


# ADD CAR
@app.post("/cars")
def add_car(car: CarCreate,
            db: Session = Depends(get_db)):

    new_car = Car(
        car_name=car.car_name,
        model=car.model,
        price_per_day=car.price_per_day,
        status=car.status
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return {
        "message": "Car Added Successfully"
    }


# UPDATE CAR
@app.put("/cars/{car_id}")
def update_car(
    car_id: int,
    updated_car: CarCreate,
    db: Session = Depends(get_db)
):

    car = db.query(Car).filter(
        Car.id == car_id
    ).first()

    if not car:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    car.car_name = updated_car.car_name
    car.model = updated_car.model
    car.price_per_day = updated_car.price_per_day
    car.status = updated_car.status

    db.commit()

    return {
        "message": "Car Updated Successfully"
    }


# DELETE CAR
@app.delete("/cars/{car_id}")
def delete_car(
    car_id: int,
    db: Session = Depends(get_db)
):

    car = db.query(Car).filter(
        Car.id == car_id
    ).first()

    if not car:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    db.delete(car)
    db.commit()

    return {
        "message": "Car Deleted Successfully"
    }

# CREATE BOOKING
@app.post("/bookings")
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    car = db.query(Car).filter(
        Car.id == booking.car_id
    ).first()

    if not car:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    new_booking = Booking(
        user_id=booking.user_id,
        car_id=booking.car_id,
        booking_date=booking.booking_date,
        return_date=booking.return_date,
        status="Active"
    )

    db.add(new_booking)

    car.status = "Booked"

    db.commit()
    db.refresh(new_booking)

    return {
        "message": "Booking Created Successfully"
    }


# VIEW ALL BOOKINGS
@app.get("/bookings")
def get_bookings(
    db: Session = Depends(get_db)
):
    return db.query(Booking).all()


# VIEW SINGLE BOOKING
@app.get("/bookings/{booking_id}")
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


# CANCEL BOOKING
@app.put("/bookings/{booking_id}/cancel")
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    booking.status = "Cancelled"

    db.commit()

    return {
        "message": "Booking Cancelled"
    }


# RETURN CAR
@app.put("/bookings/{booking_id}/return")
def return_car(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    booking.status = "Returned"

    car = db.query(Car).filter(
        Car.id == booking.car_id
    ).first()

    if car:
        car.status = "Available"

    db.commit()

    return {
        "message": "Car Returned Successfully"
    }

# DASHBOARD STATISTICS
@app.get("/dashboard")
def dashboard_stats(
    db: Session = Depends(get_db)
):

    total_cars = db.query(Car).count()

    total_bookings = db.query(
        Booking
    ).count()

    available_cars = db.query(Car).filter(
        Car.status == "Available"
    ).count()

    return {
        "total_cars": total_cars,
        "total_bookings": total_bookings,
        "available_cars": available_cars
    }