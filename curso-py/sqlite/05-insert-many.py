import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    users = [
        (2, "Cleo"),
        (3, "Freyja"),
    ]
    cursor.executemany(
        "insert into users values (?, ?)",
        users,
    )
