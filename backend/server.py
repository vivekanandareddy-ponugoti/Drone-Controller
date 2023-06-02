from flask import Flask, request, jsonify
from flask_cors import CORS
from dronekit import connect, VehicleMode
import time

app = Flask(__name__)
CORS(app)

class DroneController:
    CONNECTION_STRING = "127.0.0.1:14550"

    def __init__(self):
        """
        Constructor to create the vehicle object
        """
        self.vehicle = connect(self.CONNECTION_STRING, wait_ready=False)

    def __del__(self):
        if hasattr(self, 'vehicle'):
            self.vehicle.close()

    def arm_vehicle(self):
        """
        This method is used to arm the vehicle.
        It uses a while loop to ensure that the vehicle is armed.
        """
        self.vehicle.armed = True
        while not self.vehicle.armed:
            print('Waiting for the drone to arm.')
            time.sleep(1)
        return self.vehicle.armed

drone = DroneController()

@app.route('/arm_drone', methods=['POST'])
def arm_drone():
    try:
        print("Arming drone...")
        result = drone.arm_vehicle()
        print("Drone armed successfully.")
        return jsonify({"status": "success", "message": "Drone armed successfully"}), 200
    except Exception as e:
        print(f"Error arming drone: {str(e)}")
        return jsonify({"status": "error", "message": f"Error arming drone: {str(e)}"}), 500

@app.route('/is_drone_armed', methods=['GET'])
def is_drone_armed():
    """
    Checks to make sure that the drone is armed before allowing
    a user to change the control surfaces
    """
    try:
        status = drone.vehicle.armed
        return jsonify({"status": "success", "armed": status}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error checking drone status: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=False)
