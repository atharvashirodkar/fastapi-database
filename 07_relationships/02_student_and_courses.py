from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

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


class StudentCourse(Base):
    __tablename__ = "student_courses"

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("students.id"))

    course_id = Column(Integer, ForeignKey("courses.id"))


print("Student and Course relationship created successfully.")
