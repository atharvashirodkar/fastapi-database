import sqlite3

# Connect to the database
connection = sqlite3.connect("students.db")

# Create a cursor
cursor = connection.cursor()

# Fetch all students
cursor.execute("""
SELECT * FROM students
""")

students = cursor.fetchall()

print("Students Table:")
print()

for student in students:
    print(student)

# Close connection
connection.close()