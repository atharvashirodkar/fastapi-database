from fastapi import FastAPI

from database import SessionLocal, engine
from models import Base, Student
from schema import StudentResponse

app = FastAPI()

Base.metadata.create_all(engine)


@app.get("/students", response_model=list[StudentResponse])
def get_students():

    session = SessionLocal()

    students = session.query(Student).all()

    session.close()

    return students
