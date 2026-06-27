# 📝 SQLAlchemy CRUD Notes

## Running the Examples

Before running any examples in this module:

1. Open this module's folder in the terminal.
2. Activate the virtual environment.

   **Windows (PowerShell)**

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **Linux / macOS**

   ```bash
   source venv/bin/activate
   ```

3. Run the example files.

   Example:

   ```bash
   python 01_create_records.py
   ```

---

# 🎯 Module Objective

In the previous module, we learned how to:

```text
Create Models
Define Columns
Create Tables
```

At this point, our database structure exists.

However, the tables are empty.

A database becomes useful only when it contains data.

The goal of this module is to learn how to perform:

```text
Create
Read
Update
Delete
```

operations using SQLAlchemy.

These operations are commonly known as:

```text
CRUD
```

---

# 🗺️ The Journey So Far

SQLite Module:

```sql
INSERT INTO students ...

SELECT * FROM students ...

UPDATE students ...

DELETE FROM students ...
```

We manually wrote SQL.

---

Now we'll perform the same operations using Python objects.

Think:

```text
Before

SQL
↓
Database

Now

Python Object
↓
SQLAlchemy
↓
Database
```

This is the core idea behind an ORM.

---

# 📄 Understanding Supporting Files

Before looking at CRUD operations, let's understand the helper files used throughout this module.

---

## database.py

This file creates the database connection configuration.

Example:

```python
engine = create_engine(
    "sqlite:///students.db"
)
```

and:

```python
Session = sessionmaker(
    bind=engine
)
```

---

Think:

```text
Engine
↓
Knows How To Connect

Session
↓
Creates Sessions
```

Every CRUD file imports these objects.

Without them, SQLAlchemy cannot communicate with the database.

---

## models.py

This file contains the database models.

Example:

```python
class Student(Base):
```

The model describes:

```text
Table Name
Columns
Data Types
Constraints
```

Remember:

```text
Model
↓
Describes Data

Table
↓
Stores Data
```

---

## db_viewer.py

This file exists for learning purposes.

Internally it uses:

```sql
SELECT *
FROM students
```

to display the current contents of the database.

Example:

```python
view_students()
```

Output:

```text
(1, 'Rahul', 24)
(2, 'Priya', 22)
```

This helps us verify that SQLAlchemy actually changed the database.

Good developers verify.

They do not simply assume code worked.

---

# 📄 File-by-File Explanation

## 01_create_records.py

Run:

```bash
python 01_create_records.py
```

This file creates a new Student object.

Example:

```python
student = Student(
    name="Rahul",
    age=24
)
```

At this moment:

```text
Student Object Exists
Database Row Does Not
```

The object only exists in Python memory.

---

Next:

```python
session.add(student)
```

tells SQLAlchemy:

```text
Track this object.
I want to save it later.
```

Notice:

```text
Record Not Saved Yet
```

---

The actual save happens here:

```python
session.commit()
```

Think:

```text
Student Object
↓
Session
↓
Database Row
```

This is one of the most important ORM concepts.

---

Equivalent SQL:

```sql
INSERT INTO students (
    name,
    age
)
VALUES (
    'Rahul',
    24
);
```

---

## 02_read_records.py

Run:

```bash
python 02_read_records.py
```

This file reads records from the database.

Example:

```python
students = (
    session.query(Student)
    .all()
)
```

Think:

```text
Database Rows
↓
SQLAlchemy
↓
Student Objects
```

The process is now reversed.

Earlier:

```text
Object
↓
Database
```

Now:

```text
Database
↓
Object
```

---

Equivalent SQL:

```sql
SELECT *
FROM students;
```

---

Each result becomes:

```python
student.id
student.name
student.age
```

because SQLAlchemy converts rows into Python objects.

---

## 03_update_records.py

Run:

```bash
python 03_update_records.py
```

The first step is locating a student.

Example:

```python
student = (
    session.query(Student)
    .filter(Student.id == 1)
    .first()
)
```

Equivalent SQL:

```sql
SELECT *
FROM students
WHERE id = 1
LIMIT 1;
```

---

If the student exists:

```python
student.age = 25
```

we simply modify the object's attribute.

Notice:

```text
No UPDATE SQL written manually.
```

---

Then:

```python
session.commit()
```

saves the change.

Think:

```text
Database Row
↓
Student Object
↓
Modify Object
↓
Commit
↓
Database Updated
```

---

This is one of the biggest differences between ORM-based development and raw SQL development.

---

## 04_delete_records.py

Run:

```bash
python 04_delete_records.py
```

The first step is locating the record.

Example:

```python
student = (
    session.query(Student)
    .filter(Student.id == 1)
    .first()
)
```

After finding the object:

```python
session.delete(student)
```

marks it for deletion.

Notice:

```text
Record Still Exists
```

at this point.

---

The actual deletion occurs when:

```python
session.commit()
```

runs.

Think:

```text
Database Row
↓
Student Object
↓
Delete Request
↓
Commit
↓
Row Removed
```

---

Equivalent SQL:

```sql
DELETE FROM students
WHERE id = 1;
```

---

## 05_complete_crud.py

This file combines everything learned in the module.

Sequence:

```text
Create
↓
Read
↓
Update
↓
Read
↓
Delete
↓
Read
```

Running this file allows you to observe the complete lifecycle of a database record.

---

# 🧠 Understanding Session

By now you've probably noticed:

```python
session.add(...)
session.query(...)
session.commit(...)
session.delete(...)
```

appearing everywhere.

That's because the Session is the primary workspace used by SQLAlchemy.

Think:

```text
Session
=
Workspace For Database Operations
```

Almost every database action passes through a Session.

---

# 🧠 Understanding Commit

A common beginner mistake is thinking:

```python
session.add(student)
```

immediately inserts a record.

Not necessarily.

The change becomes permanent when:

```python
session.commit()
```

executes.

Think:

```text
add()
↓
Prepare Change

commit()
↓
Save Change
```

The same applies to:

```text
Create
Update
Delete
```

operations.

---

# 🧠 Understanding Query

Example:

```python
session.query(Student)
```

Think:

```text
I want information
from the students table.
```

---

Example:

```python
session.query(Student).all()
```

Think:

```text
Give me all students.
```

Equivalent SQL:

```sql
SELECT *
FROM students;
```

---

# 🧠 Understanding Filter

Example:

```python
.filter(Student.id == 1)
```

Think:

```sql
WHERE id = 1
```

---

Example:

```python
.filter(Student.age > 18)
```

Think:

```sql
WHERE age > 18
```

---

Filter is simply SQLAlchemy's way of narrowing down results.

---

# 🔍 Real-World Variation

In the update and delete examples, we used:

```python
.filter(Student.id == 1)
```

for simplicity.

In real applications, you may want the most recently inserted record.

Example:

```python
student = (
    session.query(Student)
    .order_by(Student.id.desc())
    .first()
)
```

Equivalent SQL:

```sql
SELECT *
FROM students
ORDER BY id DESC
LIMIT 1;
```

This returns the student with the highest ID value.

---

# 🔄 Mental Model

If you remember one thing from this module, remember this:

```text
Create

Python Object
↓
Database Row
```

```text
Read

Database Row
↓
Python Object
```

```text
Update

Object
↓
Modify
↓
Commit
```

```text
Delete

Object
↓
Delete Request
↓
Commit
```

---

# ❓ Common Beginner Questions

### Why do we need Session?

Because Session manages all database operations.

Without a Session:

```text
No Queries
No Inserts
No Updates
No Deletes
```

---

### Why do we need commit()?

Because SQLAlchemy waits until commit() before making changes permanent.

Think:

```text
Commit = Save Changes
```

---

### Does SQL still exist?

Yes.

SQLAlchemy generates SQL behind the scenes.

Understanding SQL remains extremely valuable.

---

### Is SQLAlchemy replacing SQL?

No.

SQLAlchemy is built on top of SQL concepts.

Learning SQL first was important because it helps you understand what SQLAlchemy is doing internally.

---

# 🚀 What's Coming Next?

Current Progress:

```text
SQLite + SQL
↓
SQLAlchemy Setup
↓
Models & Tables
↓
SQLAlchemy CRUD
```

Next:

```text
FastAPI + SQLAlchemy
```

You'll start connecting database operations to API endpoints and build applications that store and retrieve real data.

---

# ✅ Module Summary

In this module, you learned:

- How to create records
- How to read records
- How to update records
- How to delete records
- How Sessions work
- Why commit() is important
- How query() works
- How filter() works
- How SQLAlchemy maps Python objects to database rows

You can now perform complete CRUD operations using SQLAlchemy instead of manually writing SQL queries.