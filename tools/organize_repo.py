"""Repository organizer script

Run this script in the repository root to standardize filenames and directory names.

It will:
- Propose renames for directories with non-ASCII or spaces.
- Normalize filenames in `assets/` (lowercase, replace spaces, transliterate Turkish chars).
- Move renamed files into `assets/cleaned/` and print a manifest.

This script requires Python 3.6+ and will ask for confirmation before making changes.
"""
from __future__ import annotations
import os
import shutil
import sys
from pathlib import Path
import unicodedata


def transliterate_turkish(name: str) -> str:
    # Basic Turkish char replacements -> ASCII
    repl = {
        'İ': 'I', 'ı': 'i', 'Ş': 'S', 'ş': 's', 'Ğ': 'G', 'ğ': 'g', 'Ü': 'U', 'ü': 'u', 'Ö': 'O', 'ö': 'o', 'Ç': 'C', 'ç': 'c'
    }
    for k, v in repl.items():
        name = name.replace(k, v)
    # Normalize and remove remaining non-ASCII
    name = unicodedata.normalize('NFKD', name)
    name = ''.join(c for c in name if ord(c) < 128)
    return name


def normalize_filename(fname: str) -> str:
    # Lowercase, replace spaces with underscore, transliterate turkish, remove problematic chars
    fname = transliterate_turkish(fname)
    fname = fname.strip()
    fname = fname.replace(' ', '_')
    fname = fname.replace('-', '_')
    fname = fname.replace('(', '').replace(')', '')
    fname = fname.replace('__', '_')
    return fname.lower()


def plan_operations(root: Path) -> dict:
    ops = {}
    # Directories to rename (heuristic: non-ascii or spaces)
    for p in root.iterdir():
        if p.is_dir():
            name = p.name
            if any(ord(c) > 127 for c in name) or ' ' in name:
                new = normalize_filename(name)
                new = new.replace('__', '_')
                # Camel/Title style for directories
                new = ''.join(part.capitalize() for part in new.split('_'))
                ops[str(p)] = str(root / new)

    # Files in assets
    assets = root / 'assets'
    cleaned = assets / 'cleaned'
    if assets.exists() and assets.is_dir():
        for f in assets.iterdir():
            if f.is_file():
                new_name = normalize_filename(f.name)
                ops[str(f)] = str(cleaned / new_name)

    return ops


def confirm_and_apply(ops: dict):
    if not ops:
        print('No operations planned.')
        return
    print('Planned operations:')
    for src, dst in ops.items():
        print(f'  {src} -> {dst}')
    ans = input('\nApply these operations? [y/N]: ').strip().lower()
    if ans != 'y':
        print('Abort. No changes made.')
        return

    # Perform moves (create target directories as needed)
    for src, dst in ops.items():
        src_p = Path(src)
        dst_p = Path(dst)
        dst_p.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.move(str(src_p), str(dst_p))
            print(f'Moved: {src_p} -> {dst_p}')
        except Exception as e:
            print(f'Failed to move {src_p}: {e}')


def main():
    root = Path(__file__).resolve().parents[1]
    print(f'Repo root: {root}')
    ops = plan_operations(root)
    confirm_and_apply(ops)


if __name__ == '__main__':
    main()
