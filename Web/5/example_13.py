#!/usr/bin/env python3

import sqlite3
from pathlib import Path

db_file = str(Path(__file__).parent) + "/school.db"
conn = sqlite3.connect(db_file)

cur = conn.cursor()

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

print("########################################################")

name = input("Enter a student name: ")
sql = "SELECT * FROM students WHERE name=?"

cur.execute(sql, (name,))
rows = cur.fetchall()
for row in rows:
    print(row)

input("########################################################")

sql = "INSERT INTO students VALUES(null,?,?,?,?,?,?,?)"

cur.execute(sql, ("Akram", "1990-10-15", "Male", "Maadi", "012544789", 4, "A"))
conn.commit()

cur.execute(sql, ("Mona", "1989-03-03", "Female", "Alex", "", 4, "D"))
conn.rollback()

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

input("########################################################")

sql = "DELETE FROM students WHERE name=?"
cur.execute(sql, ("Akram",))
conn.commit()

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
