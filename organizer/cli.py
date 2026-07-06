import typer

from .commands.organize import organize_command
from .watcher import watch
from .commands.duplicates import duplicates_command

app = typer.Typer(
    help="📂 Workspace Organizer"
)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    folder: str = typer.Option(
        None,
        "--folder",
        "-f",
        help="Folder to organize",
    ),
):
    """
    Default command.
    """
    if ctx.invoked_subcommand is None:
        organize_command(folder)


@app.command()
def organize(
    folder: str = typer.Option(
        None,
        "--folder",
        "-f",
        help="Folder to organize",
    ),
):
    """
    Organize files once.
    """
    organize_command(folder)


@app.command("watch")
def watch_command(
    folder: str = typer.Option(
        None,
        "--folder",
        "-f",
        help="Folder to watch",
    ),
):
    """
    Watch a folder continuously.
    """
    from pathlib import Path

    if folder is None:
        folder = str(Path.home() / "Downloads")

    watch(Path(folder))

@app.command("duplicates")
def duplicates(
    folder: str = typer.Option(
        None,
        "--folder",
        "-f",
        help="Folder to scan for duplicate files",
    ),
):
    duplicates_command(folder)