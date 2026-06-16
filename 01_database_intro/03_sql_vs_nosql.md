# ⚔️ SQL vs NoSQL Databases

Now that you understand what databases are, let's look at the two major styles you will hear about most often.

---

## 🗄️ Two Main Types of Databases

Most databases fall into one of these two groups:

```text
SQL Databases
NoSQL Databases
```

They solve similar problems, but they organize data differently.

---

## 📊 SQL Databases

SQL stands for:

```text
Structured Query Language
```

SQL databases store data in a structured format:

```text
Tables → Rows → Columns
```

Example:

### students Table

| id | name | age |
|----|------|-----|
| 1 | Rahul | 24 |
| 2 | Priya | 22 |

Notice the pattern:

```text
Every row follows the same structure.
```

That is one of the biggest strengths of SQL databases.

---

### How SQL Feels

Think of SQL databases like this:

```text
students
├── id
├── name
└── age
```

The structure is fixed, predictable, and easy to query.

Popular SQL databases include:

- SQLite
- MySQL
- PostgreSQL
- Microsoft SQL Server
- Oracle Database

---

## 📦 NoSQL Databases

NoSQL means:

```text
Not Only SQL
```

NoSQL databases are more flexible.

Instead of tables, data may be stored as:

```text
Documents
Key-Value Pairs
Graphs
Wide Columns
```

Example document:

```json
{
    "id": 1,
    "name": "Rahul",
    "age": 24,
    "skills": [
        "Python",
        "FastAPI",
        "SQL"
    ]
}
```

Unlike SQL rows, NoSQL documents do not always need the same shape.

That flexibility is the main reason people use them.

Popular NoSQL databases include:

- MongoDB
- Redis
- Cassandra
- CouchDB
- DynamoDB

---

## 🤔 A Quick Thought Experiment

Imagine we have two students.

Student 1:

```json
{
    "name": "Rahul",
    "age": 24
}
```

Student 2:

```json
{
    "name": "Priya",
    "age": 22,
    "skills": [
        "Python",
        "FastAPI"
    ]
}
```

Question:

```text
Would this fit easily inside a SQL table?
```

Not really.

The second student contains extra information.

This is the type of situation where NoSQL databases often feel more natural.

---

## 🔍 A Quick Comparison

| Feature | SQL | NoSQL |
|----------|-----|-------|
| Structure | Fixed Schema | Flexible Schema |
| Storage | Tables | Documents / Other Formats |
| Relationships | Strong | Usually Simpler |
| Best For | Structured Data | Flexible Data |
| Examples | SQLite, PostgreSQL | MongoDB, Redis |

---

## 🎯 Which One Are We Learning Here?

In this repository, we are focusing on:

```text
SQLite
↓
SQLAlchemy
↓
FastAPI
```

That means we are learning SQL databases.

---

## 🤔 Why SQL First?

Most FastAPI applications use databases like:

- PostgreSQL
- MySQL
- SQLite

SQLAlchemy is also designed primarily around SQL databases.

Learning SQL first gives you a strong foundation because many database concepts originate from SQL systems.

---

## 🌍 Real-World Usage

### SQL Databases

Commonly used for:

```text
Banking Systems
E-Commerce Platforms
School Management Systems
Inventory Systems
ERP Applications
```

These systems usually require:

```text
Strong Relationships
Consistent Data
Reliable Transactions
```

---

### NoSQL Databases

Commonly used for:

```text
Caching
Real-Time Analytics
Chat Applications
Large-Scale Data Systems
Session Storage
```

These systems often benefit from:

```text
Flexibility
Speed
Rapid Data Changes
```

---

## ⚠️ Beginner Advice

A common beginner mistake is thinking:

```text
I need to choose SQL or NoSQL right now.
```

You don't.

Focus on learning SQL first.

Once you understand:

```text
Tables
Rows
Columns
Relationships
Queries
```

learning NoSQL becomes much easier.

---

## 🚀 Our Journey

Current Progress:

```text
Why Databases?
↓
Database Concepts
↓
SQL vs NoSQL
```

Next:

```text
SQLite
↓
SQL Queries
↓
SQLAlchemy
↓
Database APIs
```

That is the path we will follow throughout this repository.

---

## ✅ Key Takeaway

Most databases fall into two broad categories:

```text
SQL
↓
Tables + Structured Data

NoSQL
↓
Flexible Data Storage
```

For this repository, we will focus on:

```text
SQLite
SQL
SQLAlchemy
```

because they provide the strongest foundation for building database-backed FastAPI applications.