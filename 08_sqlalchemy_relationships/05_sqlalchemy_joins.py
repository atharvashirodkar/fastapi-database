from core.database import SessionLocal, engine
from core.models import Base, Student, Course, Mark

Base.metadata.create_all(engine)

session = SessionLocal()

print("\nStudent Marks Report:\n")

results = (
    session.query(Student.name, Course.name, Mark.marks)
    .join(Mark, Student.id == Mark.student_id)
    .join(Course, Course.id == Mark.course_id)
    .all()
)

for student_name, course_name, marks in results:
    print(f"{student_name} scored " f"{marks} in " f"{course_name}")

session.close()
