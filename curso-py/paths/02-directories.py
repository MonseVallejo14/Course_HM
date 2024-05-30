from pathlib import Path

path = Path("paths")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("murphy")

files = [p for p in path.iterdir() if not p.is_dir]
files = [p for p in path.glob("*.py")]
files = [p for p in path.glob("**/.py")]
files = [p for p in path.rglob("*.py")]  # "r" is for recursive.
print(files)
