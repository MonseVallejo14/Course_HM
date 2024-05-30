import sqlite3

con = sqlite3.connect("sqlite/app.db")
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists users
    (id INTEGER primary key, name VARCHAR(50));
    """
)
con.commit()
con.close()
