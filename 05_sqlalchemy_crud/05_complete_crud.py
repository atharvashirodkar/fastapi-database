from database import Session, engine
from models import Base, Student
from db_viewer import view_students

Base.metadata.create_all(engine)

session = Session()

print("\n--- CREATE ---")

student = Student(
    name="Rahul",
    age=24
)

session.add(student)

session.commit()

print("Student created successfully.")

view_students()

print("\n--- READ ---")

students = session.query(Student).all()

for student in students:
    print(
        f"ID: {student.id}, "
        f"Name: {student.name}, "
        f"Age: {student.age}"
    )

print("\n--- UPDATE ---")

student = (
    session.query(Student)
    .filter(Student.id == 1)
    .first()
)

if student:
    student.age = 25

    session.commit()

    print("Student updated successfully.")

view_students()

print("\n--- DELETE ---")

student = (
    session.query(Student)
    .filter(Student.id == 1)
    .first()
)

if student:
    session.delete(student)

    session.commit()

    print("Student deleted successfully.")

view_students()

session.close()