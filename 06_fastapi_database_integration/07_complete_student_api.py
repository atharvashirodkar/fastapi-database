from fastapi import FastAPI, HTTPException

from database import engine, SessionLocal
from models import Base, Student
from schema import StudentCreate, StudentResponse

app = FastAPI()

Base.metadata.create_all(engine)


@app.get("/students", response_model=list[StudentResponse])
def get_students():
    session = SessionLocal()

    students = session.query(Student).all()

    session.close()

    return students


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    session = SessionLocal()

    student = session.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate):
    session = SessionLocal()

    new_student = Student(name=student.name, age=student.age)

    session.add(new_student)

    session.commit()

    session.refresh(new_student)

    session.close()

    return new_student


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate):
    session = SessionLocal()

    existing_student = session.query(Student).filter(Student.id == student_id).first()

    if existing_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    existing_student.name = student.name
    existing_student.age = student.age

    session.commit()
    session.refresh(existing_student)

    session.close()

    return existing_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    session = SessionLocal()

    student = session.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    session.delete(student)
    session.commit()
    session.close()

    return {"message": "Student deleted successfully"}
