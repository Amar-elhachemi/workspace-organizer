from pathlib import Path
import typer

from .config import DEFAULT_FOLDER
from .organizer import organize

app = typer.Typer(help="Workspace Organizer")


@app.command()
def organize_files(
    folder: Path = typer.Option(
        DEFAULT_FOLDER,
        "--folder",
        "-f",
        help="Folder to organize",
    )
):
    organize(folder)


if __name__ == "__main__":
    app()