# 📝 Relationships Notes

## Running the Examples

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
   python 01_foreign_keys.py
   ```

4. For the API example:

   ```bash
   uvicorn 05_complete_relationship_api:app --reload
   ```

---

# 🎯 Module Objective

Until now, our applications mostly worked with a single table:

```text
students
```

That was enough for learning CRUD operations, but real applications rarely work with only one table.

Think about a learning platform:

```text
Rahul studies Python and FastAPI.
Priya studies Python and React.
Rahul scores 85 in Python.
```

Questions immediately appear:

```text
Which courses does Rahul study?
Who studies Python?
What marks did Rahul get?
```

A single table cannot answer these questions.

This module teaches how databases connect information using:

```text
Foreign Keys
Relationship Tables
Relationship Queries
```

and how FastAPI can expose that connected data through APIs.

---

# 🤔 Why Relationships Exist

Imagine we start with a simple table.

Students

| id | name |
|----|------|
| 1 | Rahul |
| 2 | Priya |

Looks fine.

Now Rahul joins:

```text
Python, FastAPI, Docker
```

and Priya joins:

```text
Python, React
```

A beginner might think:

| id | name | courses |
|----|------|----------|
| 1 | Rahul | Python, FastAPI, Docker |
| 2 | Priya | Python, React |

This seems simple, but problems quickly appear.

- What if a course name changes?
- What if Rahul joins another course?
- What if thousands of students exist?
- What if hundreds of courses exist?

Soon the design becomes difficult to maintain.

Databases solve this by separating information:

Students

| id | name |
|----|------|
| 1 | Rahul |
| 2 | Priya |

Courses

| id | name |
|----|--------|
| 1 | Python |
| 2 | FastAPI |
| 3 | React |

Now we have a new problem:

```text
How do we connect these tables?
```

That is exactly why relationships exist.

---

# 🧠 Understanding Foreign Keys

A Foreign Key is simply a reference to another table.

Example:

```python
student_id = Column(
    Integer,
    ForeignKey("students.id")
)
```

Think:

```text
The value stored here
must come from students.id
```

Example:

Students

| id | name |
|----|------|
| 1 | Rahul |

Marks

| id | student_id | marks |
|----|------------|-------|
| 1 | 1 | 85 |

The database understands:

```text
Student ID 1 → Rahul
```

So this row means:

```text
Rahul scored 85.
```

Foreign Keys keep relationships valid.

Without them:

```text
student_id = 999
```

could exist even though Student 999 doesn't.

---

# 🧠 Understanding Relationship Tables

Some relationships cannot be represented with a single foreign key.

Example:

```text
Student ↔ Course
```

One student can have many courses:

```text
Rahul → Python, FastAPI
```

One course can have many students:

```text
Python → Rahul, Priya
```

This is called a:

```text
Many-to-Many Relationship
```

Databases solve this using an intermediate table:

```text
student_courses
```

Example:

| student_id | course_id |
|------------|-----------|
| 1 | 1 |
| 1 | 2 |
| 2 | 1 |

Translated:

```text
Rahul → Python
Rahul → FastAPI
Priya → Python
```

The table stores only the relationships.

---

# 🧠 Understanding Relationship Queries

Creating relationships is only half the story.

Eventually someone asks:

```text
Show me Rahul's marks.
Show me Rahul's courses.
Show me all students studying Python.
```

Now we need relationship queries.

Example:

```python
session.query(Mark)\
    .filter(Mark.student_id == 1)\
    .all()
```

Think:

```text
Find all marks
belonging to Student ID 1.
```

Equivalent SQL:

```sql
SELECT *
FROM marks
WHERE student_id = 1;
```

This is usually the moment where relationships start feeling useful.

We're no longer asking:

```text
Give me a student.
```

We're asking:

```text
Give me information connected to a student.
```

---

# 🧠 Understanding Connected Data

As applications grow, tables stop behaving like isolated lists.

Instead, they become connected.

Think:

```text
Student → Courses
Student → Marks
Course → Students
```

The value of a database comes from these connections.

Without relationships:

```text
Tables are isolated.
```

With relationships:

```text
Tables can answer meaningful questions.
```

For example:

```text
Who scored 90 in FastAPI?
Which courses belong to Rahul?
Who studies Python?
```

These questions are the reason relationships exist.

---

# 🧠 Relationships and FastAPI

FastAPI itself doesn't create relationships.

Relationships are a database concept.

FastAPI simply gives us APIs to work with that connected data.

Example endpoints:

```http
POST /students
GET  /students
POST /courses
GET  /courses
POST /marks
GET  /marks
GET  /students/{student_id}/marks
```

For the first time, our API works with multiple related tables instead of a single table.

Think:

```text
Student → Course → Marks
```

instead of:

```text
Student
```

alone.

---

# 🔄 Mental Model

If you remember only one thing from this module, remember this:

```text
Students Table → Stores Students
Courses Table  → Stores Courses
Marks Table    → Stores Marks
```

Relationships connect those tables:

```text
Foreign Key        → Creates Connection
Relationship Table → Stores Many-to-Many Connections
Relationship Query → Uses Those Connections
```

The big picture is:

```text
Separate Tables
        ↓
Connected Data
        ↓
Meaningful Information
```