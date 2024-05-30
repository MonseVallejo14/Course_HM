from pathlib import Path  # To create and import paths on our computer

# Path(r"C:\Archivos de  Programa\Minecraft")  # The "r" is a Raw String so that backslashes aren't considered escape characters. This is how they are created for Windows.
# Path("/usr/bin")  # On McOS y Linux. This is a absolute path.
# Path()  # A path is created where we are.
# Path.home()
# Path("one/__init__.py")  # This is a relative path.

path = Path("Hi-World/my-file.py")
path.is_file()  # To know if it's a file
path.is_dir()  # To know if it's a directory
path.exists()  # To know if exists

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

# To change the name and the extension of the file
p = path.with_name("murphy.exe")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("happy")
print(p)
