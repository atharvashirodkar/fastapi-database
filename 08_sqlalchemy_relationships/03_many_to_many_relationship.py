from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

student_courses = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    courses = relationship(
        "Course", secondary=student_courses, back_populates="students"
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship(
        "Student", secondary=student_courses, back_populates="courses"
    )


# This association table defines the relationship structure only.
# The actual table is created when create_all() runs.
print("Many-to-many relationship created successfully.")
