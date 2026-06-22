# ❓ faq.md

This file answers some common beginner questions about SQLAlchemy.

These confusions are completely normal.

---

## Did `create_engine()` create a connection?

No.

```python
engine = create_engine(
    "sqlite:///students.db"
)
```

creates an Engine.

It does **not** create a database connection.

Think of the Engine as:

```text
Saved WiFi Configuration
```

It knows:

- Which database to use
- Where the database is located
- How to connect

But no communication has started yet.

---

## Is Engine the same as Connection?

No.

Think:

```text
Engine = Knows how to connect

Connection = Is connected
```

Example:

```python
engine = create_engine(
    "sqlite:///students.db"
)

with engine.connect() as connection:
    ...
```

The Engine creates Connections.

They are different things.

---

## Is Session the same as Connection?

No.

Think:

```text
Session = Application Workspace

Connection = Communication Channel
```

A Session internally uses Connections.

Most application code works with Sessions rather than directly managing Connections.

---

## Do FastAPI applications use Connections directly?

Sometimes.

But most application code works through Sessions.

Typical flow:

```text
User
↓
FastAPI
↓
Session
↓
Engine
↓
Database
```

Internally:

```text
Session
↓
Requests Connection from Engine
↓
Connection talks to Database
```

---

## Do I still need SQL?

Yes.

SQLAlchemy does not replace SQL.

SQLAlchemy helps organize database work.

Understanding SQL remains extremely important because SQLAlchemy generates SQL behind the scenes.

---

## Is SQLAlchemy a Database?

No.

SQLAlchemy is a Python library.

Think:

```text
SQLite
PostgreSQL
MySQL
```

These are databases.

```text
SQLAlchemy
```

is a toolkit that helps Python applications communicate with databases.

---

## Is SQLAlchemy an ORM?

Yes.

ORM stands for:

```text
Object Relational Mapper
```

An ORM translates between:

| Python | Database |
|----------|----------|
| Classes | Tables |
| Objects | Rows |
| Attributes | Columns |

Instead of writing:

```sql
INSERT INTO students ...
```

you work with Python objects.

SQLAlchemy generates SQL behind the scenes.

---

## Why didn't we start with SQLAlchemy?

Because SQLAlchemy builds on top of database concepts.

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

Now you can understand what SQLAlchemy is doing behind the scenes.

---

## Do I need to memorize `create_engine()`, `Session()`, and other syntax?

No.

Syntax can always be looked up.

Focus on understanding:

```text
Engine = Knows how to connect

Connection = Actually connected

Session = Application workspace
```

Those ideas are far more important than memorizing function names.

---

## Which should I use: Connection or Session?

For small scripts:

```python
with engine.connect():
    ...
```

may be enough.

For real applications, especially FastAPI applications, Sessions are usually preferred because they help manage:

```text
Queries
Inserts
Updates
Deletes
Transactions
```

Most SQLAlchemy application code works through Sessions.

---

## What should I remember from this module?

If you forget everything else, remember:

```text
Engine
↓ 
Connection
↓
Session
```

and understand what each one represents:

```text
Engine = Knows how to connect

Connection = Actually connected

Session = Application workspace
```

Everything else can be looked up later.