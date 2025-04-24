import sqlite3

conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS train_cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_number TEXT,
    car_type TEXT,
    capacity INTEGER
)
""")

cursor.executemany("""
INSERT INTO train_cars (car_number, car_type, capacity)
VALUES (?, ?, ?)
""", [
    ("A101", "passenger", 80),
    ("B202", "freight", 120),
    ("C303", "passenger", 100)
])

conn.commit()
conn.close()

