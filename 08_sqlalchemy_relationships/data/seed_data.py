from core.database import SessionLocal, engine
from core.models import Base, Course, Mark, Student

Base.metadata.create_all(engine)

def seed_data():
    session = SessionLocal()

    if session.query(Student).first():
        session.close()
        return

    python_course = Course(name="Python")

    fastapi_course = Course(name="FastAPI")

    rahul = Student(name="Rahul", age=24, courses=[python_course, fastapi_course])

    priya = Student(name="Priya", age=22, courses=[python_course])

    session.add_all([rahul, priya])

    session.commit()

    session.refresh(rahul)
    session.refresh(priya)

    session.refresh(python_course)
    session.refresh(fastapi_course)

    session.add_all(
        [
            Mark(student_id=rahul.id, course_id=python_course.id, marks=85),
            Mark(student_id=rahul.id, course_id=fastapi_course.id, marks=90),
            Mark(student_id=priya.id, course_id=python_course.id, marks=88),
        ]
    )

    session.commit()
    session.close()

seed_data()