# 📝 SQLite Basics Notes

## 🎯 Module Objective

In the previous module, we learned:

- Why databases exist
- Database concepts
- SQL vs NoSQL

In this module, we started working with a real database using SQLite.

By the end of this module, you'll be able to:

- Create a database
- Create tables
- Insert records
- Read records
- Update records
- Delete records

using SQL queries executed through Python.

---

## 🗄️ What Is SQLite?

SQLite is a lightweight SQL database.

Unlike MySQL or PostgreSQL:

```text
✓ No separate installation required
✓ No database server required
✓ Stores everything inside a single file
```

Example:

```text
students.db
```

This file contains:

```text
Tables
Rows
Columns
Data
```

---

## 🔌 Connecting to a Database

Create or open a database:

```python
import sqlite3

connection = sqlite3.connect("students.db")
```

If:

```text
students.db
```

does not exist, SQLite creates it automatically.

---

Close the connection:

```python
connection.close()
```

Always close database connections when you're done.

---

## 🖱️ What Is a Cursor?

A cursor executes SQL queries.

Example:

```python
cursor = connection.cursor()
```

Think of a cursor as:

```text
Python
↓
Cursor
↓
Database
```

The cursor sends SQL commands to SQLite.

---

## 🏗️ CREATE TABLE

Create a table:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
```

Result:

| id | name | age |
|----|------|-----|

An empty table is created.

---

## 🔑 PRIMARY KEY

Example:

```sql
id INTEGER PRIMARY KEY
```

Rules:

```text
✓ Unique
✓ Cannot be NULL
✓ Identifies a row
```

Example:

| id | name |
|----|------|
| 1 | Rahul |
| 2 | Priya |

---

## ➕ INSERT INTO

Insert data:

```sql
INSERT INTO students (name, age)
VALUES ('Rahul', 24)
```

Result:

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |

---

### Auto Generated IDs

Notice:

```sql
INSERT INTO students (name, age)
VALUES ('Rahul', 24)
```

We didn't provide:

```text
id
```

SQLite automatically generates it.

---

## 📖 SELECT

Retrieve data:

```sql
SELECT * FROM students
```

Result:

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |
| 2 | Priya | 22 |

---

Retrieve specific columns:

```sql
SELECT name, age FROM students
```

---

Filter records:

```sql
SELECT * FROM students
WHERE age > 23
```

---

## ✏️ UPDATE

Modify existing records:

```sql
UPDATE students
SET age = 26
WHERE name = 'Rahul'
```

Result:

Before:

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |

After:

| id | name | age |
|----|------|-----|
| 1 | Rahul | 26 |

---

### ⚠️ Importance of WHERE

Bad:

```sql
UPDATE students
SET age = 30
```

Result:

```text
Every row is updated.
```

---

## 🗑️ DELETE

Remove records:

```sql
DELETE FROM students
WHERE name = 'Amit'
```

Result:

Before:

| id | name |
|----|------|
| 1 | Rahul |
| 2 | Priya |
| 3 | Amit |

After:

| id | name |
|----|------|
| 1 | Rahul |
| 2 | Priya |

---

### ⚠️ Importance of WHERE

Bad:

```sql
DELETE FROM students
```

Result:

```text
All rows are deleted.
```

---

## 💾 commit()

Changes are not automatically saved.

Example:

```python
connection.commit()
```

This tells SQLite:

```text
Save changes permanently.
```

Usually required after:

```text
INSERT
UPDATE
DELETE
CREATE TABLE
```

---

## 👀 Viewing Database Changes

This module includes:

```text
db_utils.py
```

which contains:

```python
show_students()
```

Most example files call this function after performing database operations.

This allows you to immediately see the current state of the database.

Example:

```text
Students Table:

(1, 'Rahul', 24)
(2, 'Priya', 22)
```

As you progress through the module, observe how the table changes after:

```text
INSERT
UPDATE
DELETE
```

operations.

---

## 🔒 SQL Injection Preview

Current examples use:

```sql
INSERT INTO students (name, age)
VALUES ('Rahul', 24)
```

for simplicity.

Later, you'll learn safer parameterized queries:

```python
cursor.execute(
    """
    INSERT INTO students (name, age)
    VALUES (?, ?)
    """,
    ("Rahul", 24)
)
```

This helps prevent SQL injection vulnerabilities.

---

## 🧠 CRUD Mapping

| Operation | SQL Command |
|------------|------------|
| Create | INSERT |
| Read | SELECT |
| Update | UPDATE |
| Delete | DELETE |

---

## 🚀 What's Coming Next?

Current Progress:

```text
Database Concepts
↓
SQLite Basics
```

Next Module:

```text
SQLAlchemy Setup
```

You'll learn:

- What SQLAlchemy is
- Why ORMs exist
- Creating a database engine
- Connecting Python applications to databases using SQLAlchemy

---

## ✅ Module Summary

In this module, you learned:

- SQLite databases
- Database connections
- Cursors
- CREATE TABLE
- INSERT INTO
- SELECT
- UPDATE
- DELETE
- PRIMARY KEY
- commit()
- CRUD operations with SQL

You now understand the SQL fundamentals required for learning SQLAlchemy.