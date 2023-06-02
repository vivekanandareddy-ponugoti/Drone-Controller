import pytest
import json
from unittest.mock import MagicMock, patch

# Mock the connect function from dronekit
with patch('dronekit.connect', return_value=MagicMock()):

    from server import app as server

@pytest.fixture
def client():
    server.config['TESTING'] = True
    with server.test_client() as client:
        yield client

@pytest.fixture
def drone_controller():
    controller = MagicMock()
    controller.arm_vehicle.return_value = True
    yield controller

def test_arm_drone(client, drone_controller):
    with patch("server.drone", drone_controller):
        response = client.post('/arm_drone')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "status" in data
        assert data["status"] == "success"
        assert data["message"] == "Drone armed successfully"

def test_is_drone_armed(client, drone_controller):
    drone_controller.vehicle.armed = True
    with patch("server.drone", drone_controller):
        response = client.get('/is_drone_armed')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "status" in data
        assert data["status"] == "success"
        assert data["armed"] == True
