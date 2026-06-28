from fastapi import FastAPI

from database import SessionLocal, engine
from models import Base, Student
from schema import StudentCreate

app = FastAPI()

Base.metadata.create_all(engine)

@app.post("/students")
def create_student(student: StudentCreate):
    session = SessionLocal()

    new_student = Student(
        name = student.name,
        age = student.age
    )

    session.add(new_student)

    session.commit()

    session.refresh(new_student)

    session.close()

    return {
        "message":"Student created succesfully"
    }