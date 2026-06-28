from fastapi import FastAPI, HTTPException

from database import SessionLocal
from models import Student

app = FastAPI()


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
