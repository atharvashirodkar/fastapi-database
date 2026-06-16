# 🏗️ Basic Database Concepts

Before writing SQL queries or using SQLite, let's understand the building blocks of a database.

The good news?

You already know some of these concepts from Python.

---

## 🤔 You Already Understand Part of a Database

Consider this Python dictionary:

```python
{
    "id": 1,
    "name": "Rahul",
    "age": 24
}
```

You already know what this represents:

```text
One Student
```

A database stores the same kind of information.

The difference is:

```text
Python stores it in memory.

A database stores it permanently.
```

---

Now imagine multiple students:

```python
[
    {
        "id": 1,
        "name": "Rahul",
        "age": 24
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 22
    }
]
```

This should feel familiar.

You're looking at:

```text
A collection of students.
```

Databases store collections like this in tables.

---

## 🗄️ What Is a Database?

A database is an organized collection of data.

Think about a student management system.

It might contain:

```text
Students
Courses
Marks
```

All of that information lives inside one database.

Think:

```text
Database
=
Container

Tables
=
Things stored inside the container
```

---

## 📦 What Is a Table?

A table stores one category of data.

Example:

### Students Table

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |
| 2 | Priya | 22 |

This table stores students.

---

Another application might have:

```text
students
courses
marks
employees
products
orders
```

Notice the pattern.

Each table focuses on one type of information.

Think:

```text
Database
↓
Tables
↓
Different Categories of Data
```

---

## 📄 What Is a Row?

Look at this table:

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |
| 2 | Priya | 22 |

Question:

```text
What does Rahul's entry represent?
```

Answer:

```text
One Student
```

That entire entry is called a row.

Example:

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |

Think:

```text
Row
=
One Record
```

---

## 🏷️ What Is a Column?

Now look at the table again:

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |

Question:

```text
What information do we store
about each student?
```

Answer:

```text
id
name
age
```

These are called columns.

Think:

```text
Column = Property , Attribute , Field
```

---

Example:

| id | name | age |
|----|------|-----|

Columns:

```text
id
name
age
```

Rows:

```text
Rahul
Priya
```

---

## 🔑 What Is a Primary Key?

Imagine you want to find a specific student.

Question:

```text
Which student has roll_no = 2?
```

The database can answer immediately because:

```text
Every Roll Number is unique.
```

---

Example:

| id | name |
|----|------|
| 1 | Rahul |
| 2 | Priya |
| 3 | Amit |

Here:

```text
id
```

is the primary key.

---

A primary key must:

```text
✓ Be unique
✓ Not be empty (NULL)
✓ Identify exactly one row
```

---

Bad example:

| id | name |
|----|------|
| 1 | Rahul |
| 1 | Priya |

Now the database has a problem:

```text
Which row belongs to student 1?
```

It cannot tell.

That's why primary keys must be unique.

---

## 🔍 What Is a Query?

A query is simply a question asked to the database.

Examples:

```text
Get all students
```

```text
Get student with id = 1
```

```text
Get all courses
```

The database receives the question and returns the answer.

We'll learn how to write queries using SQL in the next module.

---

## 🔗 A Quick Preview

Later in the repository we'll have tables like:

```text
Students
Courses
Marks
```

and ask questions such as:

```text
Which courses does Rahul study?

What marks did Rahul get in Python?

Which students are enrolled in FastAPI?
```

To answer questions like these, databases connect tables together.

These connections are called relationships.

We'll learn them later in the repository.

---

## 🌍 Real-World Example

Think about an online shopping application.

It might have:

```text
Users Table
Products Table
Orders Table
```

Example:

### Users

| id | username |
|----|----------|
| 1 | atharva |
| 2 | rahul |

### Products

| id | name |
|----|------|
| 1 | Laptop |
| 2 | Keyboard |

### Orders

| id | user_id | product_id |
|----|---------|------------|
| 1 | 1 | 1 |
| 2 | 2 | 2 |

Even though the application looks complicated, it is still built using the same concepts:

```text
Database
↓
Tables
↓
Rows
↓
Columns
↓
Primary Keys
```

---

## 🧠 Mental Model

If you remember only one thing from this file, remember this:

```text
Database
↓
Tables
↓
Rows
↓
Columns
```

and:

```text
Primary Key
↓
Uniquely Identifies a Row
```

Everything else in SQL and SQLAlchemy builds on top of these ideas.

---

## ✅ Key Takeaway

A database is not a mysterious technology.

It's simply a structured way of organizing data.

Think:

```text
Python Dictionary
↓
Database Row

Python List
↓
Database Table

Multiple Tables
↓
Database
```

Once this mapping makes sense, learning SQL becomes much easier.