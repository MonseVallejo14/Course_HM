from pathlib import Path
from time import ctime

file1 = Path("files/test-file.txt")

# file1.exists() to see if the file exists
# file1.rename() to rename the file
# file1.inlink() to delete the file

print(file1.stat())  # To see some statistics of the file like size and dates
print("Access", ctime(file1.stat().st_atime))  # To see the last access date
# To see the last modification date
print("Modification", ctime(file1.stat().st_mtime))
print("Creation", ctime(file1.stat().st_ctime))  # To see the creation date
