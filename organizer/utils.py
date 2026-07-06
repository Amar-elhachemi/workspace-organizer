from pathlib import Path
from .config import CATEGORIES


def category_for(file: Path) -> str:
    ext = file.suffix.lower()

    for folder, extensions in CATEGORIES.items():
        if ext in extensions:
            return folder

    return "Others"