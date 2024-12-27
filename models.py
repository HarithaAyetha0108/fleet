from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Vehicle(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vehicle_id: str
    vehicle_type: str
    driver_name: str
    
    trips: List["Trip"] = Relationship(back_populates="vehicle")


class Trip(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vehicle_id: Optional[int] = Field(default=None, foreign_key="vehicle.id")
    trip_start_time: str
    trip_end_time: str
    trip_distance: float

    vehicle: Vehicle = Relationship(back_populates="trips")