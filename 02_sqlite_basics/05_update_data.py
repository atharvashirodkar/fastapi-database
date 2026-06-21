import sqlite3

from db_utils import show_students

# Connect to the database
connection = sqlite3.connect("students.db")

# Create a cursor
cursor = connection.cursor()

# Update student's age
cursor.execute("""
UPDATE students
SET age = 26
WHERE name = 'Rahul'
""")

# Save changes
connection.commit()

print("Student updated successfully.")

# Close connection
connection.close()

print()
print("Updated Record:")
show_students()

