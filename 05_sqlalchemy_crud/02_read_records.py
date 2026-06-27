from database import Session, engine
from models import Base, Student

Base.metadata.create_all(engine)

session = Session()

students = session.query(Student).all()

print("\nStudents:\n")

for student in students:
    print(
        f"ID: {student.id}, "
        f"Name: {student.name}, "
        f"Age: {student.age}"
    )

# print("| ID | Name  | Age |")
# print("|----|-------|-----|")
# for student in students:
#     print(f"| {student.id}  | {student.name} | {student.age}  |")

session.close()