# Intuitive Shot Flight Algorithm

Main flight controller and perception helpers used by the IEEE BTU ANKA team during Teknofest 2022 missions. The controller monitors waypoints, activates perception over the target area, computes lateral deviation from the detected target, and rewrites the mission so the payload is released on target.

## Key files

- `flight_controller.py` - DroneKit-based controller that reads missions, starts perception at the designated waypoint, updates waypoints based on perceived offset, and triggers payload release via RC channel overrides.
- `perception.py` - OpenCV helper that tracks a red target, captures the best frame, and logs bounding box data.
- `flight_logger.py` - Lightweight file logger.
- `mission_waypoints.txt`, `mission_waypoints_update.txt` - Sample missions used in testing.
- `runtime_log.txt` - Example runtime output from a flight session.
- `detection_example.png` - Sample detection frame for reference.

## Running

```powershell
pip install dronekit opencv-python numpy
cd intuitive_shot_flight_algorithm
python flight_controller.py --connect tcp:127.0.0.1:5762
```

- Use a simulator or ground station connection string suited to your setup.
- Adjust waypoint indices in `flight_controller.py` (`start_wp`, `stop_wp`, etc.) to match your mission file before flight.
