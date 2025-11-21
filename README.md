# mission-flight

Mission & Flight Software — IEEE BTU ANKA Fixed-Wing UAV Team

This repository contains mission planning and flight software developed for the IEEE BTU ANKA fixed-wing UAV team. The project was developed for participation in the Teknofest International Unmanned Aerial Vehicle Competition (we competed in 2022).

Role: I worked on the flight control and mission/engagement (shot) software.

Links:

- Team Instagram: https://www.instagram.com/ieeebtuanka/
- Teknofest - International UAV Competition: https://www.teknofest.org/en/competitions/international-unmanned-aerial-vehicle-competition/

Logo: `assets/logo.png` (placeholder file can be generated with `assets/create_logo.py`)

## Quickstart

1. Make sure you have Python 3.8+ installed.
2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. There is no `requirements.txt` yet. If you have specific dependencies, add them or let me generate `requirements.txt` for you.

4. Run the main controller script (example):

```powershell
python controller.py
```

`controller.py` contains the main control/mission loop. `detection.py` contains helper functions for detection and perception.

## Repository Layout (short)

- `controller.py` : Main flight controller and mission manager.
- `detection.py` : Image processing / target detection helpers.
- `logger.py` : Simple logging helper.
- `mission.txt`, `update_mission.txt` : Mission definitions and updates.
- `log.txt` : Example runtime log output.
- `assets/` : Static assets, including `logo.png` placeholder and helper scripts.

## Contributing

Small fixes and documentation updates: please open a pull request. For larger changes, open an issue first to discuss the proposed design.

## Notes

- We participated in the Teknofest International UAV Competition in 2022.
- If you want, I can also:
	- generate a `requirements.txt` listing the dependencies,
	- add a short demo or run script,
	- translate all docs to both English and Turkish.

If you'd like any of the above, tell me which and I'll proceed.
