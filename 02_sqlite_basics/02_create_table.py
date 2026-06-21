import sqlite3

# Connect to the database
connection = sqlite3.connect("students.db")

# Create a cursor object
cursor = connection.cursor()

# SQL query to create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Save changes
connection.commit()

print("Students table created successfully.")

# Close the connection
connection.close()