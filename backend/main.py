from fastapi import FastAPI

app = FastAPI()

# HOME

@app.get("/")
def home():
    return {"message": "Car Rental Management System"}

# REGISTER

@app.post("/register")
def register():
    return {"message": "User Registered"}

# LOGIN

@app.post("/login")
def login():
    return {"message": "Login Successful"}

# GET ALL CARS

@app.get("/cars")
def get_cars():
    return {
        "cars":[
            {
                "id":1,
                "name":"Toyota Corolla",
                "model":"2022",
                "price":5000
            }
        ]
    }

# GET SINGLE CAR

@app.get("/cars/{id}")
def get_car(id:int):
    return {"car_id":id}

# ADD CAR

@app.post("/cars")
def add_car():
    return {"message":"Car Added"}

# UPDATE CAR

@app.put("/cars/{id}")
def update_car(id:int):
    return {"message":f"Car {id} Updated"}

# DELETE CAR

@app.delete("/cars/{id}")
def delete_car(id:int):
    return {"message":f"Car {id} Deleted"}

# CREATE BOOKING

@app.post("/bookings")
def create_booking():
    return {"message":"Booking Created"}

# GET ALL BOOKINGS

@app.get("/bookings")
def get_bookings():
    return {"message":"All Bookings"}

# GET SINGLE BOOKING

@app.get("/bookings/{id}")
def get_booking(id:int):
    return {"booking_id":id}

# RETURN BOOKING

@app.put("/bookings/{id}/return")
def return_booking(id:int):
    return {"message":f"Booking {id} Returned"}

# CANCEL BOOKING

@app.put("/bookings/{id}/cancel")
def cancel_booking(id:int):
    return {"message":f"Booking {id} Cancelled"}

# DELETE BOOKING

@app.delete("/bookings/{id}")
def delete_booking(id:int):
    return {"message":f"Booking {id} Deleted"}

# DASHBOARD

@app.get("/dashboard")
def dashboard():
    return {
        "total_users":10,
        "total_cars":20,
        "total_bookings":5
    }