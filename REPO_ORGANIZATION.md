Repository Organization Plan and Instructions

What this change will do

- Normalize filenames in `assets/` (lowercase, underscores, remove non-ASCII characters).
- Move normalized assets into `assets/cleaned/`.
- Propose renames for directories with non-ASCII characters or spaces (interactive):
  - `İntuitive Shot Flight Algorithm` -> `IntuitiveShotFlightAlgorithm`
  - `pixel sapması` -> `PixelDeviation`

How to run

1. From PowerShell in the repository root (`e:\project\mission-flight`):

```powershell
python .\tools\organize_repo.py
```

2. The script will print planned operations and ask for confirmation before making changes.

Notes and safety

- The script moves files and directories. It asks for confirmation and will not run automatically.
- Binary files (PNG, JPG, PDF) are moved; no content is modified.
- After running, check the `assets/cleaned/` folder for renamed assets and verify that references in your markdown or code still point to correct paths. I can update references automatically if you want — I can search for occurrences of old filenames and update them to the new cleaned names.

Next recommended steps (I can do these for you):

1. Run the organizer script locally (it must run where the repo is).
2. After renaming, I can update code and documentation references (README, PDR) to use the cleaned asset paths.
3. I can also optionally rename or move other algorithm folders into a `src/` or `algorithms/` directory and add a top-level `docs/` folder with the PDR and the PDF report.
