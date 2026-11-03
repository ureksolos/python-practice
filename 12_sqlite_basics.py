import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        year INTEGER
    )
""")

cur.execute("INSERT INTO movies (title, year) VALUES (?, ?)", ("Inception", 2010))
cur.execute("INSERT INTO movies (title, year) VALUES (?, ?)", ("Parasite", 2019))
conn.commit()



conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("SELECT * FROM movies WHERE year > 2015")
for row in cur.fetchall():
    print(row["title"], row["year"])
conn.close()