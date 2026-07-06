from pathlib import Path

CATEGORIES = {
    "Images": [
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".bmp",
        ".webp",
        ".svg",
    ],
    "Documents": [
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".ppt",
        ".pptx",
        ".xls",
        ".xlsx",
    ],
    "Videos": [
        ".mp4",
        ".mkv",
        ".mov",
        ".avi",
        ".webm",
    ],
    "Music": [
        ".mp3",
        ".wav",
        ".flac",
        ".aac",
    ],
    "Archives": [
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
    ],
    "Code": [
        ".py",
        ".js",
        ".ts",
        ".java",
        ".cpp",
        ".c",
        ".php",
        ".html",
        ".css",
        ".json",
        ".sql",
    ],
}

DEFAULT_FOLDER = Path.home() / "Downloads"