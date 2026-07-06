from pathlib import Path
import shutil

from rich.console import Console

console = Console()

CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".json"],
}


def get_category(file: Path):
    ext = file.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category

    return "Others"


def organize_folder(folder: Path):
    if not folder.exists():
        console.print("[red]Folder not found.[/red]")
        return

    moved = 0

    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = get_category(file)

        destination = folder / category
        destination.mkdir(exist_ok=True)

        shutil.move(file, destination / file.name)

        console.print(f"✅ {file.name} → {category}")

        moved += 1

    console.print(f"\n[bold green]Moved {moved} files.[/bold green]")