import sqlite3


def view_table_schema(table_name: str):
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute(
        f"""
        PRAGMA table_info({table_name})
        """
    )

    print(f"\nSchema for '{table_name}' table:\n")

    for column in cursor.fetchall():
        print(column)

    connection.close()