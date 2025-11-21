# Algorithms and Detection Modules

This directory hosts the computer-vision demos and detection experiments that fed into the main flight stack. Each subfolder is self-contained so you can test and tune algorithms without touching the flight controller.

## Structure

- `anka_detect/` - Team-specific detection utilities and a short video demo.
- `detect_cpu/` - CPU-only detection experiments (Canny edge detector, demo scripts).
- `pixel_deviation/` - Pixel deviation experiment to estimate target offset in images.

## How to run

1) Install Python 3.8+ with OpenCV and NumPy:

```powershell
pip install opencv-python numpy
```

2) Enter a module directory and run its demo script, for example:

```powershell
cd algorithms\\anka_detect
python team_detection_demo.py
```

Each subfolder README lists the available scripts and expected inputs.
