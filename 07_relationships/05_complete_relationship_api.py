from fastapi import FastAPI, HTTPException

from database import SessionLocal, engine
from models import Base, Student, Course, Mark
from schemas import (
    StudentCreate,
    StudentResponse,
    CourseCreate,
    CourseResponse,
    MarkCreate,
    MarkResponse,
)

app = FastAPI()

Base.metadata.create_all(engine)


@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate):
    session = SessionLocal()

    new_student = Student(name=student.name, age=student.age)

    session.add(new_student)

    session.commit()

    session.refresh(new_student)

    session.close()

    return new_student


@app.get("/students", response_model=list[StudentResponse])
def get_students():
    session = SessionLocal()

    students = session.query(Student).all()

    session.close()

    return students


@app.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate):
    session = SessionLocal()

    new_course = Course(name=course.name)

    session.add(new_course)

    session.commit()

    session.refresh(new_course)

    session.close()

    return new_course


@app.get("/courses", response_model=list[CourseResponse])
def get_courses():
    session = SessionLocal()

    courses = session.query(Course).all()

    session.close()

    return courses


@app.post("/marks", response_model=MarkResponse)
def create_mark(mark: MarkCreate):
    session = SessionLocal()

    student = session.query(Student).filter(Student.id == mark.student_id).first()

    if student is None:
        session.close()

        raise HTTPException(status_code=404, detail="Student not found")

    course = session.query(Course).filter(Course.id == mark.course_id).first()

    if course is None:
        session.close()

        raise HTTPException(status_code=404, detail="Course not found")

    new_mark = Mark(
        student_id=mark.student_id, course_id=mark.course_id, marks=mark.marks
    )

    session.add(new_mark)

    session.commit()

    session.refresh(new_mark)

    session.close()

    return new_mark


@app.get("/marks", response_model=list[MarkResponse])
def get_marks():
    session = SessionLocal()

    marks = session.query(Mark).all()

    session.close()

    return marks


@app.get("/students/{student_id}/marks")
def get_student_marks(student_id: int):
    session = SessionLocal()

    student = session.query(Student).filter(Student.id == student_id).first()

    if student is None:
        session.close()

        raise HTTPException(status_code=404, detail="Student not found")

    marks = session.query(Mark).filter(Mark.student_id == student_id).all()

    result = []

    for mark in marks:
        course = session.query(Course).filter(Course.id == mark.course_id).first()

        result.append(
            {
                "student_id": student.id,
                "student_name": student.name,
                "course_id": course.id,
                "course_name": course.name,
                "marks": mark.marks,
            }
        )

    session.close()
    if result:
        return result
    return {"message":"result not found"}