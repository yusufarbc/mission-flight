# pixel_deviation

Pixel deviation experiment to estimate how far a detected target is from the image center. The results informed the in-flight waypoint corrections in the main controller.

## Files

- `pixel_deviation.py` - Computes offset metrics on a sample image.
- `target_example.png` - Example target image used by the script.

## Usage

```powershell
pip install opencv-python numpy
python pixel_deviation.py
```

Swap `target_example.png` with your own sample to test different targets.
