import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Delete data from the "students" table
student_name_to_delete = "Bob"

cursor.execute('''
    DELETE FROM students
    WHERE name = ?
''', (student_name_to_delete,))

# Commit the changes
conn.commit()

# Select and print the remaining data
cursor.execute("SELECT * FROM students")
remaining_rows = cursor.fetchall()

print("Remaining Data:")
for row in remaining_rows:
    print(row)

# Close the connection
conn.close()
