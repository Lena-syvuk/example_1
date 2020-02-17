import sqlite3

conn = sqlite3.connect("First.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  Employees                 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     first_name TEXT,
                     last_name TEXT,
                     age INTEGER,
                     type_of_employment TEXT,
                     work_phone INTEGER,
                     mobile_phone INTEGER)""")
cursor.execute("""CREATE TABLE Salary                 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      period_of_experience REAL,
                      rate REAL,
                      tax_percentage REAL,
                      FOREIGN KEY(ID) REFERENCES Employees (ID))""")
cursor.execute("""CREATE TABLE Position                 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      business_unit TEXT,
                      department TEXT,
                      current_position TEXT,
                      location TEXT,                                   
                      FOREIGN KEY(ID) REFERENCES Employees (ID))""")
conn.commit()
cursor.close()
conn.close()
