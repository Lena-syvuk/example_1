import sqlite3

conn = sqlite3.connect("second.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE phone_book               
                    (id INTEGER  PRIMARY KEY AUTOINCREMENT,
                     first_name TEXT NOT NULL,
                     last_name TEXT NOT NULL,
                     phone_number INTEGER NOT NULL)""")

conn.commit()
cursor.close()
conn.close()