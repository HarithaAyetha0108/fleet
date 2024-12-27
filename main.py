from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from models import Vehicle, Trip
from database import get_db

app = FastAPI()

@app.post("/vehicles/")
def create_vehicle(vehicle: Vehicle, db: Session = Depends(get_db)):
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

@app.get("/vehicles/")
def get_all_vehicles(db: Session = Depends(get_db)):
    return db.exec(select(Vehicle)).all()

# @app.post("/trips/")
# def create_trip(trip: Trip, db: Session = Depends(get_db)):
#     vehicle = db.get(Vehicle, trip.vehicle_id)
#     if not vehicle:
#         raise HTTPException(status_code=404, detail="Vehicle not found")
#     db.add(trip)
#     db.commit()
#     db.refresh(trip)
#     return trip

# @app.get("/trips/")
# def get_all_trips(db: Session = Depends(get_db)):
#     return db.exec(select(Trip)).all()

# @app.get("/vehicles/{vehicle_id}/trips/")
# def get_trips_for_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
#     vehicle = db.get(Vehicle, vehicle_id)
#     if not vehicle:
#         raise HTTPException(status_code=404, detail="Vehicle not found")
#     return vehicle.trips