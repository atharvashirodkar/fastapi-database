from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    age = Column(Integer)


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)

    name = Column(String)


class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("students.id"))

    course_id = Column(Integer, ForeignKey("courses.id"))

    marks = Column(Integer)

# If you think why I didn't import the above classes from another file, 
# It's because Python modules cannot be imported if the filename starts with a number (e.g., `123module.py` is invalid).

# following code creates a SQLite database named "students.db" 
# and sets up a session to interact with it. 

engine = create_engine("sqlite:///students.db")

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

session = SessionLocal()

students = session.query(Student).all()

print("\nStudents:\n")

for student in students:
    print(student.name)

courses = session.query(Course).all()

print("\nCourses:\n")

for course in courses:
    print(course.name)

# It queries all students, courses, and marks for a specific student (with ID 1) and prints the results.
student_marks = session.query(Mark).filter(Mark.student_id == 1).all()

print("\nMarks For Student ID 1:\n")

for mark in student_marks:
    print(f"Course ID: {mark.course_id}, " f"Marks: {mark.marks}")

session.close()
