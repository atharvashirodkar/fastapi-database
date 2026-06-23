# 📝 Models and Tables Notes

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
   python 01_first_model.py
   ```

---

# 🎯 Module Objective

In the previous module, we learned:

```text
Engine
Connection
Session
```

These components helped us understand how SQLAlchemy communicates with a database.

In this module, we'll answer a different question:

```text
How does SQLAlchemy know
what tables should exist?
```

Instead of manually writing SQL table definitions, we'll start describing database structures using Python classes.

---

# 🗺️ The Journey So Far

In the SQLite module, we manually created tables.

Example:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
```

Whenever we wanted a new table, we had to write another SQL statement.

---

Now we'll start writing:

```python
class Student(Base):
    ...
```

instead.

Think:

```text
Before

SQL
↓
Table

Now

Python Class
↓
SQLAlchemy
↓
Table
```

The goal of this module is to understand how SQLAlchemy converts Python classes into database tables.

---

# 📄 File-by-File Explanation

## 01_first_model.py

Run:

```bash
python 01_first_model.py
```

Output:

```text
Student model created successfully.
```

At first glance, you might think:

```text
Did SQLAlchemy create a table?
```

Not yet.

This file only introduces the idea of a model.

Example:

```python
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
```

This class describes:

```text
Table Name
Columns
Data Types
Constraints
```

but nothing has been created inside the database yet.

Think:

```text
Model = Blueprint

Table = Actual Structure
```

Just because a blueprint exists doesn't mean the building has been constructed.

---

## 02_table_schema.py

This file focuses on the structure of a table.

You'll see:

```python
id = Column(Integer)

name = Column(String)

age = Column(Integer)
```

A common beginner mistake is treating these as normal Python variables.

They're not.

Each attribute describes a column that SQLAlchemy should create later.

---

When you see:

```python
name = Column(String)
```

read it as:

```text
Create a column named "name"
that stores text values.
```

---

When you see:

```python
age = Column(Integer)
```

read it as:

```text
Create a column named "age"
that stores whole numbers.
```

---

A useful mental translation is:

```text
Python Class
↓
Database Table

Python Attribute
↓
Database Column
```

Example:

```python
class Student(Base):
    id = Column(Integer)
    name = Column(String)
```

becomes:

| id | name |
|----|------|

inside the database.

---

## 03_create_tables.py

Run:

```bash
python 03_create_tables.py
```

Output:

```text
Table created successfully.
```

This is the first file that actually creates something inside the database.

The important line is:

```python
Base.metadata.create_all(engine)
```

SQLAlchemy reads every model connected to:

```python
Base
```

and generates the required SQL automatically.

---

Conceptually:

```python
class Student(Base):
    ...
```

becomes:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    age INTEGER
);
```

behind the scenes.

---

The biggest shift here is:

```text
You describe the table in Python.

SQLAlchemy writes the SQL.
```

You no longer manually write:

```sql
CREATE TABLE ...
```

for every table.

---

## 04_multiple_models.py

Real applications rarely have only one table.

A school management system doesn't only contain students.

It also contains:

```text
Courses
Marks
Teachers
Attendance
```

and much more.

---

This file introduces multiple models.

Example:

```python
class Student(Base):
    ...

class Course(Base):
    ...

class Mark(Base):
    ...
```

Instead of one table:

```text
students
```

the application now has:

```text
students
courses
marks
```

which is much closer to how real databases are designed.

---

# 🧠 Understanding Models

A model is a Python class that describes how a database table should look.

Example:

```python
class Student(Base):
    __tablename__ = "students"
```

The model itself does not store data.

Its job is only to define:

```text
Table Name
Columns
Data Types
Rules
```

Think:

```text
Model
↓
Describes Table

Table
↓
Stores Data
```

---

# 🧠 Understanding __tablename__

Example:

```python
__tablename__ = "students"
```

This tells SQLAlchemy:

```text
When creating a table,
use the name "students".
```

Without:

```python
__tablename__
```

SQLAlchemy would not know what table name to create.

---

# 🧠 Understanding Columns

A table is made up of rows and columns.

Example:

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |
| 2 | Priya | 22 |

---

In this table:

```text
id
name
age
```

are columns.

Columns define what information can be stored.

---

When we write:

```python
name = Column(String)
```

we're telling SQLAlchemy:

```text
Create a column named "name"
and allow text values to be stored in it.
```

Similarly:

```python
age = Column(Integer)
```

means:

```text
Create a column named "age"
and allow whole numbers to be stored in it.
```

---

Think:

```text
Python Attribute
↓
Database Column
```

---

# 🧠 Understanding Data Types

Data types define what kind of information a column can store.

---

## Integer

Example:

```python
age = Column(Integer)
```

Used for:

```text
18
21
35
50
```

Equivalent SQL:

```sql
INTEGER
```

---

## String

Example:

```python
name = Column(String)
```

Used for:

```text
Rahul
Priya
Amit
```

Equivalent SQL:

```sql
VARCHAR
```

---

Choosing the correct data type is important because it helps the database store and validate data correctly.

---

# 🧠 Understanding Primary Keys

Example:

```python
id = Column(
    Integer,
    primary_key=True
)
```

Every table usually needs a way to uniquely identify each row.

That's the job of a primary key.

Example:

| id | name |
|----|------|
| 1 | Rahul |
| 2 | Priya |

Good:

```text
1
2
```

Bad:

```text
1
1
```

because primary keys must be unique.

---

Think:

```text
Primary Key = Unique Identity of a Row
```

Similar to how an Aadhaar number uniquely identifies a person.

---

# 🔍 Verifying What SQLAlchemy Created

When learning SQLAlchemy, it's easy to trust that everything worked.

However, good developers verify.

That's why this module includes:

```python
view_table_schema("students")
```

Internally, it uses SQLite's:

```sql
PRAGMA table_info(students)
```

command.

This allows us to inspect the actual table structure created by SQLAlchemy.

---

Example Output:

```text
(0, 'id', 'INTEGER', 1, None, 1)
(1, 'name', 'VARCHAR', 0, None, 0)
(2, 'age', 'INTEGER', 0, None, 0)
```

Notice how the database structure matches:

```python
id = Column(Integer, primary_key=True)
name = Column(String)
age = Column(Integer)
```

This is an important moment.

For the first time, you can clearly see:

```text
Python Model
↓
SQLAlchemy
↓
Actual Database Table
```

working together.

---

# 🧠 Understanding Foreign Keys

In:

```python
class Mark(Base):
```

you'll see:

```python
student_id = Column(
    Integer,
    ForeignKey("students.id")
)
```

and:

```python
course_id = Column(
    Integer,
    ForeignKey("courses.id")
)
```

At first, this may look confusing.

Let's simplify it.

---

Imagine:

Students Table

| id | name |
|----|------|
| 1 | Rahul |
| 2 | Priya |

Courses Table

| id | name |
|----|------|
| 1 | Python |
| 2 | FastAPI |

Marks Table

| id | student_id | course_id | marks |
|----|------------|------------|-------|
| 1 | 1 | 1 | 90 |
| 2 | 1 | 2 | 85 |

---

Notice:

```text
student_id
```

contains values from:

```text
students.id
```

and:

```text
course_id
```

contains values from:

```text
courses.id
```

This creates a relationship between tables.

Think:

```text
A Mark belongs to a Student

A Mark belongs to a Course
```

Foreign Keys help databases maintain valid relationships between records.

---

# 🔄 Mental Model

If you remember only one thing from this module, remember this:

```text
Model
↓
Blueprint

Table
↓
Actual Database Structure
```

and:

```text
Python Class
↓
Database Table

Python Attribute
↓
Database Column
```

Everything in SQLAlchemy models builds on these ideas.

---

# ❓ Common Beginner Questions

### Did creating a model create a table?

No.

Example:

```python
class Student(Base):
```

only defines the structure.

The table is created later using:

```python
Base.metadata.create_all(engine)
```

---

### Is a model the same as a table?

Not exactly.

Think:

```text
Architectural Blueprint
↓
Model

Constructed Building
↓
Table
```

One describes.

The other exists.

---

### Why use Python classes instead of SQL?

Because Python classes are easier to organize, reuse, maintain, and scale as applications grow.

Instead of maintaining dozens of CREATE TABLE statements, we maintain Python models.

---

### Does SQL still exist?

Yes.

SQLAlchemy generates SQL behind the scenes.

Learning SQL is still important because SQLAlchemy is built on top of database concepts.

---

# 🚀 What's Coming Next?

Current Progress:

```text
SQLite + SQL
↓
Engine
↓
Connection
↓
Session
↓
Models
↓
Tables
```

Next:

```text
Database CRUD
```

You'll start:

```text
Creating Records
Reading Records
Updating Records
Deleting Records
```

using SQLAlchemy instead of raw SQL.

---

# ✅ Module Summary

In this module, you learned:

- What a model is
- How models represent tables
- How columns are defined
- Common SQLAlchemy data types
- Primary keys
- Foreign keys
- How tables are created
- How multiple models work together
- How to verify generated table schemas

You can now describe database structures using Python classes and allow SQLAlchemy to generate the database tables for you.