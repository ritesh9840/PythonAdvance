import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table in the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        score INTEGER
    )
''')

# Insert some data into the table
students_data = [
    ("Alice", 25, 95),
    ("Bob", 30, 85),
    ("Charlie", 22, 90)
]

cursor.executemany('''
    INSERT INTO students (name, age, score)
    VALUES (?, ?, ?)
''', students_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into 'example.db' successfully.")

# Now, let's read data from the database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Select all data from the students table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# Print the retrieved data
print("Retrieved Data:")
for row in rows:
    print(row)

# Close the connection
conn.close()
