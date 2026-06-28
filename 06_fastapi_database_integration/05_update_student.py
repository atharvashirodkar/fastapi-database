from fastapi import FastAPI, HTTPException

from database import SessionLocal
from models import Student
from schema import StudentCreate, StudentResponse

app = FastAPI()


@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):
    session = SessionLocal()

    existing_student = session.query(Student).filter(Student.id == student_id).first()

    if existing_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    existing_student.name = student.name
    existing_student.age = student.age

    session.commit()
    session.close()

    return {"message": "Student updated successfully"}
