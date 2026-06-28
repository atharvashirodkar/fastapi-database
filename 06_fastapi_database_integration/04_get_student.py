from fastapi import FastAPI

from database import SessionLocal, engine
from models import Base, Student
from schema import StudentCreate, StudentResponse

app = FastAPI()

Base.metadata.create_all(engine)


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):

    session = SessionLocal()

    student = session.query(Student).filter(Student.id == student_id).first()

    session.close()
    
    return student