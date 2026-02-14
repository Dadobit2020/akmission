#!/usr/bin/env python3
import sys
import shutil
from pathlib import Path

if len(sys.argv) != 3:
    print("Usage: python save_image.py <source> <destination>")
    sys.exit(1)

source = Path(sys.argv[1])
dest = Path(sys.argv[2])

if not source.exists():
    print(f"Error: Source file {source} does not exist")
    sys.exit(1)

dest.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(source, dest)
print(f"Successfully copied {source} to {dest}")
print(f"File size: {dest.stat().st_size} bytes")
