from database import Session as SessionLocal, engine
from models import Base, Student
from db_viewer import view_students

Base.metadata.create_all(engine)

session = SessionLocal()

student = Student(
    name="Rahul",
    age=24
)

session.add(student)

session.commit()

session.close()

print("Student created successfully.")

view_students()