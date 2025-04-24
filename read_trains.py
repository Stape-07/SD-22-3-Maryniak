import sqlite3

conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM train_cars")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

