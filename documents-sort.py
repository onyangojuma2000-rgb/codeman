from __future__ import annotations


import argparse
import shutil
from datetime import datetime 
from pathlib import Path 


FOLDER_BY_EXTENSION = {
    ".docx": "contracts",
    ".doc": "Contracts",
    ".jpg": "Evidene",
    ".jpeg": "Evidence",
    ".png": "Evidence",
    ".pdf": "Fillings",
    ".txt": "Correspondence",
    ".eml": "correspondence",
}

def unique_destination(destination: Path) -> Path:
    """Avoid overwriting files with duplicate names."""
    if not destination.exists():
        return destination

    stem, suffix = destination.stem, destination.suffix
    counter = 1

    while True:
        candidate = destination.with_name(f"{stem}_{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def sort_folders(target: Path, log_path: Path | None = None) -> int:
    """Sort files and log every move."""
    target = target.expanduser().resolve()

    if not target.exists() or not target.is_dir():
        raise NotADirectoryError(f"Target folder does not exist: {target}")

    log_path = (log_path or target / "sort_log.txt").expanduser().resolve()
    moved = 0

    # Get files before creating destination folders.
    files = [
        item for item in target.iterdir()
        if item.is_file() and item.resolve() != log_path
    ]

    for source in files:
        category = FOLDER_BY_EXTENSION.get(source.suffix.lower(), "Other")
        category_dir = target / category
        category_dir.mkdir(exist_ok=True)

        destination = unique_destination(category_dir / source.name)
        shutil.move(str(source), str(destination))

        timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
        with log_path.open("a", encoding="utf-8") as log:
            log.write(f"{timestamp} | FROM: {source} | TO: {destination}\n")

        moved += 1

    return moved


def main():
    parser = argparse.ArgumentParser(
        description="Sort legal documents by file extension."
    )
    parser.add_argument(
        "folder",
        type=Path,
        help="Folder containing unsorted files",
    )

    args = parser.parse_args()
    try:
        moved = sort_folders(args.folder)
    except OSError as exc:
        parser.error(str(exc))

    print(
        f"Sorting complete. Moved {moved} file(s). "
        f"Log: {args.folder.expanduser().resolve() / 'sort_log.txt'}"
    )


if __name__ == "__main__":
    main()