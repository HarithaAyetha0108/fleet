from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_vehicles():
    vehicle_data = {
        "vehicle_id": "V12345",
        "vehicle_type": "Bus",
        "driver_name": "John Doee"
    }
    client.post("/vehicles/", json=vehicle_data)

    response = client.get("/vehicles/")
    assert response.status_code == 200



