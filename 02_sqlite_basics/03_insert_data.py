from db_utils import show_students
import sqlite3

# Connect to the database
connection = sqlite3.connect("students.db")

# Create a cursor
cursor = connection.cursor()

# Insert student records
cursor.execute("""
INSERT INTO students (name, age)
VALUES ('Rahul', 24)
""")

cursor.execute("""
INSERT INTO students (name, age)
VALUES ('Priya', 22)
""")

cursor.execute("""
INSERT INTO students (name, age)
VALUES 
    ('Amit', 25)
    ('Rahul', 25)
""")

# Save changes
connection.commit()

print("Student records inserted successfully.")

# Close connection
connection.close()


show_students()
