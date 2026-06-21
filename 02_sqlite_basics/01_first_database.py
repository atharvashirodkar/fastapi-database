import sqlite3

# Create (or open) a SQLite database file
connection = sqlite3.connect("students.db")

print("Database connected successfully.")

# Always close the connection
connection.close()

print("Database connection closed.")