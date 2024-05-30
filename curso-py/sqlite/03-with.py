import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists users
        (id INTEGER primary key, name VARCHAR(50));
        """
    )

# "with" calls the magic method "__exit__" that call "commit" and "close" automatically
