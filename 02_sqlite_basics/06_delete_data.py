import sqlite3

from db_utils import show_students

# Connect to the database
connection = sqlite3.connect("students.db")

# Create a cursor
cursor = connection.cursor()

# Delete a student
cursor.execute("""
DELETE FROM students
WHERE name = 'Amit'
""")

# Save changes
connection.commit()

print("Student deleted successfully.")

# Verify remaining records
print()
print("Remaining Students:")
show_students()