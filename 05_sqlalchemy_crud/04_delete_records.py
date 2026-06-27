from database import SessionLocal, engine
from models import Base, Student
from db_viewer import view_students

Base.metadata.create_all(engine)

session = SessionLocal()

student = (
    session.query(Student)
    .filter(Student.id == 3)
    .first()
)

if student:
    session.delete(student)

    session.commit()

    print("Student deleted successfully.")

else:
    print("Student not found.")

session.close()

view_students()