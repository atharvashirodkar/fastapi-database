# ⚙️ Installing SQLAlchemy

In the previous module, we worked directly with SQLite using:

```python
import sqlite3
```

We learned how to:

- Create databases
- Create tables
- Insert records
- Read records
- Update records
- Delete records

using raw SQL queries.

---

# 🎯 The Big Question

At this point, a reasonable question is:

```text
SQLite already works.

Why am I learning SQLAlchemy?
```

Before learning any new tool, it's important to understand the problem it solves.

This file exists to answer that question.

---

# 🗺️ The Journey So Far

So far, we've progressed through several ways of storing and managing data.

```text
Python Lists
↓
JSON Files
↓
SQLite + SQL
↓
SQLAlchemy
```

Each step solved problems introduced by the previous step.

---

## Python Lists

Example:

```python
students = [
    {
        "id": 1,
        "name": "Rahul"
    }
]
```

Problem:

```text
Data disappears when the application stops.
```

---

## JSON Files

Example:

```json
[
    {
        "id": 1,
        "name": "Rahul"
    }
]
```

Problem solved:

```text
Data persists between application runs.
```

New problems:

```text
Slow for large datasets
No relationships
No querying capabilities
No data integrity
```

---

## SQLite + SQL

Example:

```sql
SELECT * FROM students
```

Problem solved:

```text
Structured storage
Queries
Relationships
Data integrity
```

At this point, we can build real applications.

---

# 😫 The Problem We Are About to Face

Let's imagine our application grows.

Today:

```text
students
```

Tomorrow:

```text
students
courses
marks
teachers
attendance
fees
departments
```

---

Reading data:

```python
cursor.execute("""
SELECT * FROM students
""")
```

---

Inserting data:

```python
cursor.execute("""
INSERT INTO students (name, age)
VALUES ('Rahul', 24)
""")
```

---

Updating data:

```python
cursor.execute("""
UPDATE students
SET age = 25
WHERE id = 1
""")
```

---

Deleting data:

```python
cursor.execute("""
DELETE FROM students
WHERE id = 1
""")
```

---

Now imagine:

```text
10 tables
100+ queries
Multiple developers
Several API endpoints
```

Questions become harder:

```text
Where is this query used?
Which file contains this query?
Did I update every related query?
Is this query still needed?
```

The problem is no longer SQL itself.

The problem becomes:

```text
Managing SQL at scale.
```

---

# 🏗️ How SQLAlchemy Helps

SQLAlchemy provides tools that help organize database code.

Think of it as:

```text
Python
↓
SQLAlchemy
↓
Database
```

Instead of manually handling every database operation, SQLAlchemy provides a structured way to work with databases.

---

# 🔍 What Is an ORM?

ORM stands for:

```text
Object Relational Mapper
```

Don't worry about the name.

Focus on the idea.

---

Database Row:

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |

---

Python Object:

```python
Student(
    name="Rahul",
    age=24
)
```

---

An ORM helps connect:

```text
Python Objects
↓
Database Records
```

without forcing us to manually manage every SQL query.

---

# ⚠️ Why Didn't We Learn SQLAlchemy First?

Another common beginner question:

```text
If SQLAlchemy is so useful,
why didn't we start with it?
```

Because SQLAlchemy is built on top of database concepts.

Before learning SQLAlchemy, you needed to understand:

```text
Tables
Rows
Columns
Primary Keys
SQL Queries
CRUD Operations
```

Otherwise SQLAlchemy would feel like magic.

---

For example:

```python
session.query(Student).all()
```

looks simple.

But behind the scenes, SQLAlchemy eventually generates SQL.

Because you already know SQL, you can understand what is happening underneath.

---

# ⚠️ SQLAlchemy Does Not Replace SQL

A common misconception:

```text
SQLAlchemy means I don't need SQL anymore.
```

Wrong.

SQL still exists underneath.

Example:

```python
session.query(Student).all()
```

eventually becomes a SQL query.

This is why learning raw SQL first was important.

---

# 📦 Installing SQLAlchemy

Activate the virtual environment for this module.

Install SQLAlchemy:

```bash
pip install sqlalchemy
```

---

Verify the installation:

```bash
pip show sqlalchemy
```

Example:

```text
Name: SQLAlchemy
Version: 2.x.x
```

---

# 🧪 Verify Installation

Open Python:

```bash
python
```

Import SQLAlchemy:

```python
import sqlalchemy
```

If no error appears, the installation was successful.

Exit Python:

```python
exit()
```

---

# 🎯 What Should I Learn From This Module?

Do not focus on memorizing:

```python
create_engine(...)
```

or:

```python
sessionmaker(...)
```

Those can always be looked up later.

Instead, focus on understanding:

```text
What is an Engine?
What is a Connection?
What is a Session?
Why do they exist?
How do they work together?
```

Understanding these concepts is far more important than remembering syntax.

---

# 🚀 What We'll Learn Next

This module focuses on the fundamental building blocks of SQLAlchemy.

You'll learn:

```text
Engine
↓
Database Connection
↓
Session
```

These concepts appear in almost every SQLAlchemy application.

---

# 🗺️ Learning Roadmap

Current Progress:

```text
Python Lists
↓
JSON Files
↓
SQLite + SQL
↓
SQLAlchemy Setup
```

Next:

```text
Engine
↓
Connection
↓
Session
```

Later:

```text
Models
↓
Tables
↓
Database CRUD
↓
FastAPI Integration
```

---

# ✅ Key Takeaway

You are not learning SQLAlchemy because SQLite is bad.

You are learning SQLAlchemy because applications become larger over time.

SQLAlchemy helps organize database code, manage complexity, and work with databases in a way that scales much better than manually writing every SQL query throughout an application.

The goal of this module is to understand the foundational concepts that make that possible.