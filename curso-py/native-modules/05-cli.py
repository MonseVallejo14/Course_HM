import os
from pathlib import Path
import sys

print(sys.argv)


def cli(args):
    if len(args) == 1:
        print("No arguments passed")
        return
    if len(args) != 3:
        print("Two arguments are needed")
        return

    origin = args[1]
    o = Path(origin)
    if not o.exists():
        print("Origin doesn't exist")
        return

    destiny = args[2]
    d = Path(destiny)
    if d.exists():
        print("Destiny cannot exist")
        return

    os.rename(str(origin), str(destiny))
    print("The file was renamed successfully")


cli(sys.argv)
