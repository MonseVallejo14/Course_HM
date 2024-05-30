from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencies = {
    "db": "Data Base",
    "api": "This is the api",
    "graphql": "This is graphql"
}


def load(p):
    package = __import__(str(p).replace("/", "."))
    try:
        package.init(**dependencies)
    except:
        print("The package haven't function init")


list(map(load, paths))
