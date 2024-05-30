from pathlib import Path
from zipfile import ZipFile

# To create a zip file
# with ZipFile("files/compressed.zip", "w") as zip:
#     # curso-py
#     for path in Path().rglob("*.*"):
#         print(path)
#         if path != Path("files/compressed.zip"):
#             zip.write(path)

# To read a zip file
with ZipFile("files/compressed.zip", "r") as zip:
    #     print(zip.namelist())
    info = zip.getinfo("files/06-compressed.py")
    print(
        info.file_size,
        info.compress_size
    )
    zip.extractall("files/decompressed.py")
