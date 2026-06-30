import sqlite3

def show_tables():
    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table';
        """)

    tables =[]
    for table in cursor.fetchall():
        tables.append(table[0])
    conn.close()
    return tables

print("debug: ",show_tables())

def view_table():
    tables = show_tables()
    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()
    for table in tables:
        cursor.execute(f"""
            SELECT * FROM {table}
        """)
    
        print(f"\n {table} Table:")

        for table in cursor.fetchall():
            print(table)

    conn.close()

view_table()