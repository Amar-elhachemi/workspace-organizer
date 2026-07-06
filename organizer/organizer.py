from pathlib import Path
import shutil

from rich.console import Console
from rich.progress import track

from .utils import category_for

console = Console()


def organize(directory: Path):
    if not directory.exists():
        console.print("[red]Folder does not exist.[/red]")
        return

    files = [f for f in directory.iterdir() if f.is_file()]

    moved = 0

    for file in track(files, description="Organizing..."):
        category = category_for(file)

        destination = directory / category
        destination.mkdir(exist_ok=True)

        shutil.move(str(file), str(destination / file.name))
        moved += 1

    console.print(f"\n[green]Done![/green] Moved {moved} files.")