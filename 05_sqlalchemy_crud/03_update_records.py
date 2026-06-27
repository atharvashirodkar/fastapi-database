from database import Session, engine
from models import Base, Student
from db_viewer import view_students

Base.metadata.create_all(engine)

session = Session()

student = (
    session.query(Student)
    .filter(Student.id == 2)
    .first()
)

if student:
    student.name = "Sakshi"

    session.commit()

    print("Student updated successfully.")

else:
    print("Student not found.")

session.close()

view_students()