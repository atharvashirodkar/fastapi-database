# 📝 SQLAlchemy Setup Notes

## 📚 Quick Start

Before running any examples:

1. Open this module's folder in the terminal.

2. Create a virtual environment.

### Windows (PowerShell)

```powershell
python -m venv venv
```

### Linux / macOS

```bash
python3 -m venv venv
```

3. Activate the virtual environment.

### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source venv/bin/activate
```

4. Install SQLAlchemy.

```bash
pip install sqlalchemy
```

Optional:

```bash
pip freeze > requirements.txt
```

5. Run example files.

```bash
python 02_first_engine.py
```

---

# 🎯 Module Objective

In the previous module, we worked directly with SQLite using:

```python
import sqlite3
```

We created databases, tables, inserted records, updated records, deleted records, and executed SQL queries.

Now we're going to learn SQLAlchemy.

Before moving forward, ask yourself:

```text
If SQLite already works,
why am I learning SQLAlchemy?
```

This module is designed to answer that question.

---

# 🗺️ The Journey So Far

```text
Python Lists
↓
JSON Files
↓
SQLite + SQL
↓
SQLAlchemy
```

Each step solved problems introduced by the previous one.

---

## Python Lists

Example:

```python
students = [
    {"id": 1, "name": "Rahul"}
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
No querying
No relationships
No constraints
Not suitable for large applications
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

So why move beyond SQLite?

---

# 😫 The Problem We're About To Face

Imagine your application grows.

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

Soon you have:

```text
10+ tables
100+ SQL queries
20+ API endpoints
```

You'll find yourself writing:

```python
cursor.execute("""
SELECT * FROM students
""")
```

```python
cursor.execute("""
INSERT INTO students (...)
""")
```

```python
cursor.execute("""
UPDATE students (...)
""")
```

```python
cursor.execute("""
DELETE FROM students (...)
""")
```

throughout the application.

The problem is no longer SQL.

The problem becomes:

```text
Managing SQL.
```

That's where SQLAlchemy helps.

---

# 🏗️ Why We're Learning SQLAlchemy

SQLAlchemy helps organize:

- Database connections
- Sessions
- Models
- Queries
- Relationships

As applications grow, this structure becomes increasingly valuable.

---

# 🔍 What Is an ORM?

ORM stands for:

```text
Object Relational Mapper
```

Think of it as a translator between two worlds.

| Python World | Database World |
| ------------ | -------------- |
| Classes      | Tables         |
| Objects      | Rows           |
| Attributes   | Columns        |

Instead of writing:

```sql
INSERT INTO students (name, age)
VALUES ('Rahul', 24);
```

you work with Python objects:

```python
new_student = Student(
    name="Rahul",
    age=24
)

session.add(new_student)
session.commit()
```

SQLAlchemy generates the SQL behind the scenes.

---

# 🤔 Why Didn't We Learn SQLAlchemy First?

Because SQLAlchemy is built on top of database concepts.

Before learning SQLAlchemy, you needed to understand:

```text
Tables
Rows
Columns
Primary Keys
CRUD Operations
SQL Queries
```

Without that foundation, SQLAlchemy would feel like magic.

Now that you understand SQL, you'll be able to understand what SQLAlchemy is doing behind the scenes.

---

# ⚙️ Understanding Engine, Connection, and Session

These three concepts are commonly confused.

Let's simplify them.

---

## Engine

Think:

```text
Database Configuration
```

Example:

```python
# sqlite:// → SQLite database
# /students.db → Database file name
engine = create_engine(
    "sqlite:///students.db"
)
```

The Engine knows:

```text
Database Type
Database Location
Connection Configuration
```

The Engine knows how to connect.

It is not connected yet.

---

## Connection

Think:

```text
Active Communication Channel
```

Example:

```python
with engine.connect() as connection:
```

Without a Connection:

```text
No communication occurs.
```

---

## Session

Think:

```text
Application Workspace
```

Example:

```python
session = Session()
```

A Session helps manage:

```text
Queries
Inserts
Updates
Deletes
Transactions
```

Most real applications work with Sessions rather than Connections.

---

# 🧠 Mental Model

If you remember only one diagram from this module, remember this:

```text
FastAPI Application
        │
        ▼
     Session
        │
        ▼
      Engine
        │
        ▼
     Database
```

Internally:

```text
Session
↓
Requests Connection from Engine
↓
Connection Communicates with Database
```

---

# 📦 Installing SQLAlchemy

Install:

```bash
pip install sqlalchemy
```

Optional:

```bash
pip freeze > requirements.txt
```

Verify:

```bash
pip show sqlalchemy
```

Or from Python:

```python
import sqlalchemy

print(sqlalchemy.__version__)
```

---

# 🎯 What Should You Remember?

Six months from now, you'll probably forget:

```python
create_engine(...)
sessionmaker(...)
```

and that's okay.

What matters is remembering:

```text
Engine = Knows how to connect

Connection = Actually connected

Session = Workspace used by application code
```

Syntax can always be looked up later.

---

# 🚀 What's Coming Next?

```text
Models
↓
Tables
↓
Database CRUD
↓
Relationships
↓
FastAPI Integration
```

---

# 📄 Additional Files

For detailed walkthroughs of each example file, see:

```text
file-by-file-explanation.md
```

For common beginner questions, see:

```text
faq.md
```

---

# ✅ Module Summary

In this module, you learned:

- Why we're moving beyond raw sqlite3
- Why SQLAlchemy exists
- What an ORM is
- Why we didn't start with SQLAlchemy
- What an Engine is
- What a Connection is
- What a Session is
- How they work together
- How FastAPI applications typically interact with databases

You now have the conceptual foundation required to start building models and tables using SQLAlchemy.