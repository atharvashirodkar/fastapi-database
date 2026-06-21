import sqlite3


def show_students():
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    try:
        cursor.execute("""
        SELECT * FROM students
        """)

        students = cursor.fetchall()

        print("\nStudents Table:\n")

        if not students:
            print("No records found.")

        for student in students:
            print(student)

    except sqlite3.OperationalError:
        print("\nStudents table does not exist yet.")

    finally:
        connection.close()


show_students()
