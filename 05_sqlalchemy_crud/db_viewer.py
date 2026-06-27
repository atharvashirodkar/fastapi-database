import sqlite3

def view_students():
    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM students
    """)
    
    print("\n Student Table:")

    for student in cursor.fetchall():
        print(student)

    conn.close()