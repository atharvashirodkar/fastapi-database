# 📝 SQLAlchemy Relationships Notes

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

3. Seed the database once.

   ```bash
   python -m data.seed_data
   ```

4. Run the examples.

   Example:

   ```bash
   python 05_sqlalchemy_joins.py
   ```

5. Inspect the database if needed.

   ```bash
   python -m utils.db_viewer
   ```

---

# 🎯 Module Objective

Until now, our tables mostly lived independent lives.

```text
students
courses
marks
```

Each table could be queried separately and everything worked fine.

But real applications quickly raise questions like:

```text
Which courses does Rahul study?
Who studies Python?
Who scored 85 in Python?
```

Suddenly, one table is no longer enough.

This module answers an important question:

```text
How do tables work together?
```

or, more importantly:

```text
How do we represent real-world connections inside a database?
```

---

# 🗺️ The Story So Far

Our journey has been:

```text
SQLite → Engine → Session → Models → CRUD → FastAPI
```

Until now, we mostly treated tables as separate boxes.

This module changes the way we think about data.

Instead of isolated tables:

```text
students
courses
marks
```

we start seeing:

```text
Student → Marks → Course
Student ↔ Course
```

The database is becoming a network of connected information.

---

# 🧠 Why Relationships Exist

Imagine these tables:

Students

| id | name |
|----|------|
| 1 | Rahul |

Courses

| id | name |
|----|--------|
| 1 | Python |

Marks

| id | student_id | course_id | marks |
|----|------------|------------|-------|
| 1 | 1 | 1 | 85 |

Now ask yourself:

```text
Who scored 85 in Python?
```

The `marks` table cannot answer that alone.

It only knows:

```text
student_id = 1
course_id = 1
marks = 85
```

The actual names live in other tables.

As applications grow, tables start depending on each other. That dependency is called a **relationship**.

Without relationships, tables are isolated islands.

With relationships:

```text
Student → Marks
Student ↔ Courses
Course  → Students
```

the data becomes meaningful.

---

# 🧠 Understanding Different Types of Relationships

Real-world data can connect in different ways, so databases support different relationship types.

## One-to-One

One record belongs to exactly one other record.

Example:

```text
Person ↔ Passport
```

One person has one passport, and one passport belongs to one person.

---

## One-to-Many

One record can have many related records.

Examples:

```text
Account → Transactions
Student → Marks
```

One account can have many transactions.

One student can have many marks.

---

## Many-to-Many

This is the relationship we used in this module.

```text
Student ↔ Course
```

A student can study many courses, and a course can have many students.

A single foreign key cannot represent this relationship, so we introduce an extra table:

```text
student_courses
```

which stores only the connections.

---

# 🧠 Understanding `relationship()`

At this point, you might wonder:

```text
We already have Foreign Keys.
Why do we need relationship()?
```

That's a very good question.

Suppose we load:

```python
mark = session.query(Mark).first()
```

Python sees:

```text
id = 1
student_id = 1
marks = 85
```

But Python does not automatically know:

```text
student_id = 1 → Rahul
course_id = 1 → Python
```

It only sees numbers.

Think:

```text
ForeignKey()   → Connects database tables
relationship() → Connects Python objects
```

Now SQLAlchemy understands things like:

```python
mark.student
student.marks
student.courses
```

instead of forcing us to manually search every time.

The purpose of `relationship()` is simple:

```text
Turn related table rows into connected Python objects.
```

---

# 🧠 Understanding `back_populates`

The name looks complicated, so let's simplify it.

```text
back      = opposite direction
populate  = fill with data
```

Together, think:

```text
Connect both directions.
```

Example:

```text
Student.courses ↔ Course.students
```

If Rahul knows:

```text
Rahul → Python
```

then Python should also know:

```text
Python → Rahul
```
In simple words, back_populates connects two relationship() fields so that changes on one side of a SQLAlchemy relationship are automatically reflected on the other side in memory.

That two-way understanding is what `back_populates` provides.

Without it, SQLAlchemy may know one side of the relationship but not the other.

---

# 🧠 Understanding Association Tables

Many-to-many relationships need an extra table.

For example:

```text
Student ↔ Course
```

cannot be represented with a single foreign key.

So we create:

```text
student_courses
```

Example:

| student_id | course_id |
|------------|-----------|
| 1 | 1 |
| 1 | 2 |
| 2 | 1 |

This means:

```text
Rahul → Python
Rahul → FastAPI
Priya → Python
```

The table stores relationships only.

---

# 🧠 Understanding JOINs

Sometimes one table is not enough.

Suppose we want:

```text
Rahul scored 85 in Python.
```

No single table contains that information.

We need data from:

```text
students + courses + marks
```

A JOIN combines information from multiple tables and produces one meaningful result.

Think:

```text
Multiple Tables → One Combined Result
```

---

# 🧠 JOINs vs Relationships

These concepts are related but different.

```text
JOIN           → Reporting and combined queries
relationship() → Navigating connected objects
```

Examples:

```python
student.courses
course.students
```

are relationship navigation.

Examples like:

```text
Rahul scored 85 in Python.
```

usually involve JOINs.

---

# 🧠 Understanding Seed Data

As relationships become more complex, creating records manually becomes tedious.

That is why we created:

```text
data/seed_data.py
```

Running:

```bash
python -m data.seed_data
```

creates:

```text
Students
Courses
Marks
Relationships
```

so that every example file can focus on learning concepts instead of repeatedly inserting data.

---

# 🧠 Understanding Database Inspection

Sometimes things don't work the way we expect.

Questions start appearing:

```text
Was the table created?
Was the data inserted?
Is student_courses populated?
```

Instead of guessing, inspect the database directly.

That is why I creeated a utility file:

```text
utils/db_viewer.py
```

It lets us see the actual state of the database.

---

# 🔄 Mental Model

If you remember only one thing from this module, remember this:

```text
ForeignKey()     → Database understands relationships
relationship()   → Python understands relationships
back_populates   → Both directions stay connected
Association Table→ Stores many-to-many connections
JOIN             → Combines information from multiple tables
```

The entire module is really about one idea:

```text
Moving from isolated tables
           ↓
      Connected data
```