# Drone Controller Mobile App

## Project Brief
The aim of this software project is to develop a mobile application that eliminates the need for a separate remote controller, enabling users to control drones using their smartphones or tablets. The project seeks to revolutionize drone control, making it more accessible, affordable, and user-friendly.

## Ardupilot Simulator Setup
1. Clone the ArduPilot repository in the simulator directory and run the ArduPlane SITL simulator:
`git clone https://github.com/ArduPilot/ardupilot.git`
`cd ardupilot`
`git submodule update --init --recursive`
`cd tools/autotest`
`python3 sim_vehicle.py -v ArduPlane --console --map --out 127.0.0.1:14550`

## Functional requirements:
The mobile app will have the following functional requirements:

1. Arming Procedure: Before taking flight, users must complete a pre-flight arming procedure to ensure that all control surfaces and systems are operational.

2. Throttle Control: Similar to a gas pedal in an automobile, users can regulate the drone's engine power output by moving the left hand up and down. The throttle control has a percentage range, allowing for incremental increases or decreases in power output.

3. Rudder Control: The app will provide a separate control input for directing the drone. Users can adjust the rudder by moving the left hand right or left. The rudder control determines the aircraft's vertical axis direction.

4. Elevator/Pitch Control: The right hand will be used to regulate the drone's pitch, allowing users to adjust the nose up or down. The elevator/pitch control is adjusted by moving the right hand up or down within a percentage range, enabling gradual changes.

5. Aileron Control: The app will include a control input for modifying the drone's roll. Users can move their right hand right or left to adjust the ailerons, affecting the aircraft's roll or tilt.

6. Independent Control: The throttle, rudder, elevator/pitch, and aileron controls will operate independently of each other, allowing users to fine-tune power, direction, angle, and roll according to their preferences.

7. Measurement in Percentages: The app will present the throttle, rudder, elevator/pitch, and aileron controls in percentage format. This enables users to make precise modifications within a predefined range, with each percentage increase or reduction corresponding to a specific change in the flight parameter.

By incorporating these functional requirements, our mobile app will empower the youth program participants to control drones effectively, fostering their passion for drone flying and providing them with a valuable skill set for their future careers.
