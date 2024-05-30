from pathlib import Path

file1 = Path("files/test-file.txt")
# text = file1.read_text() Takes it as a single string
# ".split" is a method for strings to separate, "\n" indicates line break
text = file1.read_text("utf-8").split("\n")
text.insert(0, "Hi world!")
# "join" is to convert the list to a string
file1.write_text("\n".join(text), "utf-8")
print(text)
