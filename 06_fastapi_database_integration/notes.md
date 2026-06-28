# 📝 FastAPI Database Integration Notes

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

3. Start the FastAPI server.

   Example:

   ```bash
   uvicorn 01_first_database_api:app --reload
   ```

4. Open Swagger UI:

   ```text
   http://localhost:8000/docs
   ```

---

# 🎯 Module Objective

In the previous module, we learned how to perform:

```text
Create • Read • Update • Delete
```

operations directly from Python scripts.

That was useful, but there was one limitation:

```text
Only Python programs could access the database.
```

Real applications work differently.

A client sends an HTTP request:

```http
POST /students
```

The application receives the request, talks to the database, and sends back a response.

This module combines:

```text
FastAPI + Pydantic + SQLAlchemy
```

into one complete application.

---

# 🗺️ The Journey So Far

FastAPI Foundations:

```text
HTTP Requests → Responses → Path Parameters → Request Bodies → Response Models
```

FastAPI Database:

```text
SQLite → SQLAlchemy Setup → Models & Tables → CRUD
```

Now we combine both worlds:

```text
HTTP Request → FastAPI → Pydantic → SQLAlchemy → Database
```

This architecture is used by many real-world FastAPI applications.

---

# 🧠 Why Database Integration Matters

Imagine you already have a database with student information.

Without FastAPI, only Python scripts can access it.

With FastAPI:

```text
Mobile App
Web App
Desktop App
Another Backend Service
```

can all communicate with your database through HTTP APIs.

This is why database integration is important.

Instead of:

```text
Python Script → Database
```

we now have:

```text
Client → API → Database
```

The API becomes the bridge between users and data.

---

# 🧠 Understanding The Request Flow

Let's follow a request.

Client sends:

```http
POST /students
```

with:

```json
{
    "name": "Rahul",
    "age": 24
}
```

The request travels like this:

```text
Client
→ FastAPI
→ StudentCreate Schema
→ Student Model
→ Session
→ Database
```

When the database responds:

```text
Database
→ SQLAlchemy Model
→ Response Model
→ JSON
→ Client
```

This request-response cycle is the foundation of most FastAPI applications.

---

# 🧠 Models vs Schemas

A common beginner question is:

```text
Why do we need both?
```

Because they solve different problems.

```text
SQLAlchemy Model → Database Structure
Pydantic Schema  → API Validation
```

Example:

```python
class Student(Base):
```

describes:

```text
How the table looks.
```

Example:

```python
class StudentCreate(BaseModel):
```

describes:

```text
What data the client is allowed to send.
```

Think:

```text
Model  → Database Rules
Schema → API Rules
```

Both are important, and both have different responsibilities.

---

# 🧠 Understanding response_model

Example:

```python
response_model=StudentResponse
```

This tells FastAPI:

```text
Validate Response
Filter Fields
Generate Documentation
```

Think:

```text
Request Schema  → Incoming Data
Response Schema → Outgoing Data
```

The response model acts like a final checkpoint before data leaves your API.

---

# 🧠 Understanding session.refresh()

Inside:

```python
create_student()
```

you'll see:

```python
session.add(new_student)
session.commit()
session.refresh(new_student)
```

Why do we need `refresh()`?

Imagine we create:

```python
Student(
    name="Rahul",
    age=24
)
```

At this point:

```text
id = ?
```

because the database has not generated it yet.

After:

```python
session.commit()
```

the database creates:

```text
id = 1
```

But our Python object may still contain old information.

So we call:

```python
session.refresh(new_student)
```

to reload the latest values from the database.

Think:

```text
add()     → Prepare
commit()  → Save
refresh() → Reload
```

---

# 🧠 Understanding HTTPException

Suppose we request:

```http
GET /students/100
```

but student `100` does not exist.

Without error handling:

```python
student = None
```

which can lead to unexpected behavior.

Instead:

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

returns:

```http
404 Not Found
```

This is how professional APIs communicate errors.

Think:

```text
Problem
↓
Meaningful HTTP Response
```

instead of:

```text
Problem
↓
Application Crash
```

---

# 🧠 Understanding Database Sessions

A Session is SQLAlchemy's way of talking to the database.

Example:

```python
session = SessionLocal()
```

Think of it as:

```text
Open Conversation with Database
```

Through this conversation, we can:

```text
Create Records
Read Records
Update Records
Delete Records
```

When the work is finished:

```python
session.close()
```

closes that conversation.

In real applications, every request usually gets its own database session.

---

# 🔄 Mental Model

If you remember only one thing from this module, remember these two flows:

```text
Request
→ Schema
→ Model
→ Database
```

and

```text
Database
→ Model
→ Response Model
→ JSON Response
```

Everything in this module follows these flows.

The big picture is:

```text
Client
↓
FastAPI
↓
Database
↓
FastAPI
↓
Client
```

You now have everything needed to build APIs that store and retrieve real data from a database.