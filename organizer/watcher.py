from pathlib import Path
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from rich import print

from .core.mover import organize_folder


TEMP_EXTENSIONS = {
    ".crdownload",
    ".part",
    ".tmp",
    ".download",
}


class DownloadHandler(FileSystemEventHandler):
    def __init__(self, folder: Path):
        self.folder = folder

    def on_created(self, event):
        if event.is_directory:
            return

        file = Path(event.src_path)

        # Ignore temporary browser files
        if file.suffix.lower() in TEMP_EXTENSIONS:
            return

        # Wait until the file is finished writing
        if not self.wait_until_ready(file):
            return

        print(f"[green]📥 {file.name} detected[/green]")

        try:
            organize_folder(self.folder)
        except Exception as e:
            print(f"[red]{e}[/red]")

    def wait_until_ready(self, file: Path, timeout=120):
        start = time.time()
        previous_size = -1
        stable = 0

        while time.time() - start < timeout:

            if not file.exists():
                time.sleep(1)
                continue

            try:
                size = file.stat().st_size

                if size == previous_size:
                    stable += 1
                else:
                    stable = 0

                previous_size = size

                # Same size for 3 seconds = finished
                if stable >= 3:
                    return True

            except PermissionError:
                pass

            time.sleep(1)

        return False


def watch(folder: Path):
    observer = Observer()

    observer.schedule(
        DownloadHandler(folder),
        str(folder),
        recursive=False,
    )

    observer.start()

    print(f"[bold green]👀 Watching[/bold green] {folder}")
    print("[yellow]Press CTRL+C to stop[/yellow]")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[red]Stopping watcher...[/red]")
        observer.stop()

    observer.join()