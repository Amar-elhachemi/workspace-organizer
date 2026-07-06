from pathlib import Path

import typer
from rich.console import Console

from ..core.mover import organize_folder

console = Console()


def organize_command(
    folder: Path = typer.Option(
        Path.home() / "Downloads",
        "--folder",
        "-f",
        help="Folder to organize",
    )
):
    console.rule("[bold cyan]Workspace Organizer")
    organize_folder(folder)