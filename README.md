# 📂 Workspace Organizer

A Python tool that organizes your files automatically.

GitHub: https://github.com/Amar-elhachemi/workspace-organizer

---

## 🚀 Features

- Organize files (images, videos, docs, etc.)
- Watch folder and auto-organize
- Detect duplicate files

---

## 📦 Installation

```bash
git clone https://github.com/Amar-elhachemi/workspace-organizer.git
cd workspace-organizer
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
````

---

## ⚙️ Usage

### Organize folder

```bash
python -m organizer organize --folder "C:\Users\YourName\Downloads"
```

### Watch folder

```bash
python -m organizer watch --folder "C:\Users\YourName\Downloads"
```

### Find duplicates

```bash
python -m organizer duplicates --folder "C:\Users\YourName\Downloads"
```

---

## 📌 Roadmap

* Better speed optimization
* GUI version
* Windows installer (.exe)
* Publish to pip

---

## 🛠 Tech

* Python
* Typer
* Watchdog
