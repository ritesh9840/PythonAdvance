import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Update data in the "students" table
new_score = 100
student_name_to_update = "Alice"

cursor.execute('''
    UPDATE students
    SET score = ?
    WHERE name = ?
''', (new_score, student_name_to_update))

# Commit the changes
conn.commit()

# Select and print the updated data
cursor.execute("SELECT * FROM students")
updated_rows = cursor.fetchall()

print("Updated Data:")
for row in updated_rows:
    print(row)

# Close the connection
conn.close()
