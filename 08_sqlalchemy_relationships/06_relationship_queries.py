from core.database import SessionLocal, engine
from core.models import Base, Student, Course
from data.seed_data import seed_data

Base.metadata.create_all(engine)

session = SessionLocal()

print("\nStudents And Their Courses:\n")

students = session.query(Student).all()

for student in students:
    print(f"\n{student.name}")

    for course in student.courses:
        print(f"  - {course.name}")

print("\n\nCourses And Their Students:\n")

courses = session.query(Course).all()

for course in courses:
    
    print(f"\n{course.name}")

    for student in course.students:
        print(f"  - {student.name}")

session.close()