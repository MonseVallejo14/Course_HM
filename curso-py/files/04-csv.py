import csv
import os

# To write
# with open("files/file1.csv", "w") as file1:
#     writer = csv.writer(file1)
#     writer.writerow(["tweet_id", "user_id", "text"])
#     writer.writerow([1000, 1, "This is a tweet"])
#     writer.writerow([1001, 2, "Another tweet"])

# To read
# with open("files/file1.csv") as file1:
#     reader = csv.reader(file1)
#     print(list(reader))
#     file1.seek(0)
#     for line in reader:
#         print(line)

# To update
with open("files/file1.csv") as r, open("files/temp-file.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for line in reader:
        if line[0] == "1000":
            writer.writerow([1000, 1, "Modified tweet"])
        else:
            writer.writerow(line)
os.remove("files/file1.csv")
os.rename("files/temp-file.csv", "files/file1.csv")
