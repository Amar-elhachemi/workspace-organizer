from pathlib import Path
import hashlib
import typer


def file_hash(path: Path) -> str:
    """Return the SHA256 hash of a file."""
    sha256 = hashlib.sha256()

    with path.open("rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()


def duplicates_command(
    folder: str = typer.Option(
        None,
        "--folder",
        "-f",
        help="Folder to scan for duplicate files",
    )
):
    if folder is None:
        folder = str(Path.home() / "Downloads")

    folder_path = Path(folder)

    if not folder_path.exists():
        typer.secho("❌ Folder does not exist.", fg=typer.colors.RED)
        raise typer.Exit()

    typer.secho(f"🔍 Scanning {folder_path}...", fg=typer.colors.CYAN)

    hashes = {}
    duplicates = {}

    for file in folder_path.rglob("*"):
        if not file.is_file():
            continue

        try:
            h = file_hash(file)

            if h in hashes:
                duplicates.setdefault(h, [hashes[h]])
                duplicates[h].append(file)
            else:
                hashes[h] = file

        except Exception:
            continue

    if not duplicates:
        typer.secho("\n✅ No duplicate files found.", fg=typer.colors.GREEN)
        return

    typer.secho("\n📄 Duplicate files found:\n", fg=typer.colors.YELLOW)

    for files in duplicates.values():
        size = files[0].stat().st_size / (1024 * 1024)

        typer.secho(f"Size: {size:.2f} MB", fg=typer.colors.BLUE)

        for file in files:
            typer.echo(f" • {file}")

        typer.echo("-" * 60)