# Connect with sqlite database
# Import necessary libraries
import sqlite3
import pandas as pd

# Connect to database (creates one if it doesn't exist)
conn = sqlite3.connect('database.sqlite')

print("Opened database successfully")

# Create a new table in the given database with mentioned constraints
conn.execute('''CREATE TABLE CLASS_10
(SNO INT PRIMARY KEY NOT NULL,
 Roll_No INT NOT NULL,
 Name TEXT NOT NULL,
 AGE INT DEFAULT 15,
 Gender TEXT NOT NULL,
 Email_ID TEXT NOT NULL,
 Contact_No REAL NOT NULL);''')

print("Table created successfully")

# Enter data for 3 different entries
conn.execute("""INSERT INTO CLASS_10 (SNO, Roll_No, NAME, AGE, Gender, Email_ID, Contact_No)
                VALUES (1, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8088900 );""")

conn.execute("""INSERT INTO CLASS_10 (SNO, Roll_No, NAME, AGE, Gender, Email_ID, Contact_No)
                VALUES (2, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900 );""")

conn.execute("""INSERT INTO CLASS_10 (SNO, Roll_No, NAME, AGE, Gender, Email_ID, Contact_No)
                VALUES (3, 3, 'Jeff', 15, 'Male', 'allen@gmail.com', 9990900 );""")

# Save the changes
conn.commit()
print("Records created successfully")

# Display all the tables of this database
tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conn)

print(tables)

# Read table from the database into a dataframe
class_10d = pd.read_sql("""SELECT *
                           FROM CLASS_10;""", conn)

print(class_10d.head())