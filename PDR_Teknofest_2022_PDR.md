# Preliminary Design Review (PDR)
## Teknofest 2022 — International Unmanned Aerial Vehicle Competition

Project: Mission & Flight Software for a fixed-wing UAV (IEEE BTU ANKA)

Date: 2022 (competition year)

---

1. Team Organization

- Team: IEEE BTU ANKA Fixed-Wing UAV Team
- Role (author): Flight control and mission / payload delivery software development
- Notes: For the full team list, roles, and contact information, add an appendix with names and responsibilities.

2. Current Problem

During a potential conflict scenario, fires may ignite along the front line. Such fires endanger soldiers, combat vehicles, and civilians, and can cause significant loss of life and property. Extinguishing these fires may be impossible while under direct enemy fire.

(In this context, "enemy" is any entity presenting a threat to civilians or the nation.)

3. Proposed Solution

This project proposes a mission in which an autonomous fixed-wing UAV temporarily disrupts the enemy line to enable safe firefighting actions. The UAV carries two mission payloads: a smoke payload (to create a diversion or obscuration) and a water payload (to suppress or extinguish the fire). The vehicle will fly an autonomous mission and release the two payloads over two predefined rectangular target zones.

- Payloads: two discrete loads (1× smoke, 1× water)
- Mission autonomy: route upload from ground control station, automatic execution after a short manual takeoff window

4. Detailed Description of the Mission

This section describes pre-flight, flight, and post-flight procedures; the UAV characteristics; and the mission sequence. Figures and tables referenced below should be added to this document (maps, flight diagram, payload mechanism drawings, mass/power tables).

4.1 Mission Area and Target Zones

- The mission requires a flight area defined by the ground control station/competition map.
- Two rectangular release zones sized 10 m × 25 m are placed anywhere along the mission route: one marked blue (smoke release) and one marked red (water release).

Figure placeholder: mission route map with two 10 m × 25 m rectangles (blue and red).

4.2 Pre-Flight

- Prepare the UAV and payloads on the bench, verify payload fixtures and release servos, and confirm center of gravity.
- Perform standard pre-flight technical checks (airframe, control surfaces, servos, battery state, telemetry link, ground station connection).
- Arm the vehicle and perform a manual takeoff. After 5 seconds of stable climb and confirmation, switch to AUTO mode and begin the autonomous mission.

4.3 Autonomous Flight Sequence

1. UAV follows the pre-uploaded route from the ground control station (Mission Planner recommended).
2. Upon reaching the first target zone (blue), the smoke payload is released via the onboard release mechanism.
3. Upon reaching the second target zone (red), the water payload is released.
4. After both payloads are released, the mission is complete. The UAV returns and lands manually.

Figure placeholder: UAV flight diagram showing takeoff point, route, blue and red release zones, return path, and landing point.

4.4 UAV Characteristics (design summary)

- Configuration: Conventional wing and tail (mid-wing layout with conventional tail chosen for stability, controllability, and ease of production).
- Fuselage: Dimensions 417 × 55 × 55 mm (designed to house selected electronics while keeping a minimal envelope). Primary material: plywood (low cost, easy fabrication).
- Wings: Airfoil selected: USA-35B (profile chosen after AirfoilTools review). Wing area: 0.17 m². Wingspan: 1412 mm. Mean chord / characteristic wing length: 150 mm. Wingtip geometry: tapered (to reduce tip vortices).
- Tail: Conventional tail surfaces attached to fuselage via carbon-fiber tube for stiffness and light weight.
- Landing gear: To reduce fuselage damage on landing, a lightweight landing gear is used. Manufactured from 3D-printed PLA components and steel wire (balance of lightness and strength).

4.5 Mission (Payload Release) Mechanism

- Two servo-actuated release gates hold the payloads. The mechanism is plywood to minimize cost and weight while preserving structural rigidity.
- The mechanism is positioned and balanced to avoid shifting the aircraft center of gravity during release.

Figure placeholder: payload release mechanism drawings and mounting positions.

5. Reports on Mission Fulfillment

This section should gather the engineering data used to select components and verify mission success, including: mass breakdown, lift and drag calculations, propulsion and battery selection, electrical power budgets, servo and actuator specifications, structural component materials and mass, and relevant software modules.

5.1 Payload Location and System Description

Design choices were driven by payload mass, drag, ease of production, and cost. The mid-wing and conventional tail configuration was selected.

Fuselage: Sized to fit electronics, with consideration for center of gravity range. Material: plywood.

Wings: Designed for stability, reduced drag, and sufficient lift. USA-35B airfoil chosen; wing area and span given above. Taper towards wingtips to reduce induced drag.

Landing gear: Simple, robust design using 3D-printed PLA and steel wire.

Mission mechanism: Two servo motors hold the payloads; release commanded by the flight controller at the predefined GPS waypoints or when entering the defined rectangular zone.

Table placeholder: Mechanical parts, materials, dimensions, quantities, mass (fill in for mass report).

5.2 UAV Mass Report

Provide mass (weight) entries for:
- Airframe (fuselage, wings, tail)
- Flight controller and avionics
- Propulsion (motor, ESC, propeller)
- Battery (type, capacity, mass)
- Payloads (smoke and water simulants) and release mechanism
- Landing gear and hardware

Table placeholder: mass breakdown (g) and total take-off weight (kg).

5.3 Flight Report With Payload

Flight time depends on planned flight distance and cruise speed.

Formulas used:
- Airtime (t) = Flight Distance (X) / Flight Speed (V)

Given values from mission planning:
- Planned flight distance (one lap): approximately 400 m (Mission Planner measurement). The mission requires the UAV to fly the route twice, so total route distance is ~800 m.
- Cruise speed chosen: 15 m/s (above estimated stall speed).

Estimated autonomous flight time calculation:

- Autonomous route distance: 800 m
- Cruise speed: 15 m/s
- Autonomous flight time = 800 / 15 ≈ 53.3 s (reported as ≈ 54 s)
- Add manual takeoff and landing margin → planned total endurance: ≈ 75 s

Notes: These numbers are preliminary and must be validated with a full mass and power budget and flight testing.

5.4 Electrical Power Budget

Power and energy calculations follow these formulas:
- Power (W) = Current (A) × Voltage (V)
- Energy spent (J) = Flight time (s) × Spent power (W)

Procedure:
1. Collect current draw and operating voltage for each component (motor, ESC, servos, flight controller, telemetry, payload actuators).
2. Compute each component's power consumption and sum to get total cruise power.
3. Multiply total cruise power by planned flight time to get required energy (J) or convert to mAh for battery sizing.

Table placeholder: electrical component list with Voltage (V), Current (A), Power (W), and energy for planned time (J, Wh, mAh).

5.5 Flight Controller and Software Block Diagram

Provide block diagrams describing the flight controller inputs, sensors, actuators, and software modules (autopilot, mission manager, payload manager, telemetry, safety/RTB behavior).

Figure placeholder: block diagram showing sensor suite (IMU, GPS, barometer), flight controller, radio/telemetry link, payload release interface (servo outputs), and ground control station.

6. Component Selection

List and justify chosen components for motors, ESCs, battery, servos for the payload mechanism, flight controller board, GPS module, telemetry radio, and the structural materials. Include supplier part numbers, cost estimates, and test reports where available.

---

Appendices and Next Steps (work items to complete this PDR):

1. Add mass table with measured or estimated masses for all components and compute the final take-off weight and center-of-gravity (CG) envelope.
2. Add electrical component datasheets and complete the power budget and battery selection.
3. Add mechanical drawings and photos for the payload release mechanism.
4. Add mission map and Mission Planner screenshot showing route and distance calculations.
5. Add flight test results (hover/runway tests) and log extracts demonstrating the vehicle meets speed and endurance targets.

Requests for the author / team:
- Provide the component list and masses used in the design.
- Provide motor/ESC specifications and battery used or planned.
- Provide any images, CAD drawings, or Mission Planner route files (.waypoints) to embed in the report.

If you want, I can:
- Generate the mass and power tables from a provided parts CSV or spreadsheet.
- Add the Mission Planner screenshots into the `assets/` folder and link them here.
- Create a simple block diagram SVG or PNG and add it to `assets/`.
