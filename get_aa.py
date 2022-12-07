from pathlib import Path

ART_DIR = Path(__file__).absolute().parent / "ascii_art"


def get_art(name):
    with Path.open(ART_DIR / name, "r", encoding="utf-8") as f:
        return f.read()
