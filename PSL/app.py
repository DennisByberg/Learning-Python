from pathlib import Path

path = Path(r"C:\Program Files\Microsoft")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path.with_name("file.txt")
print(path)
