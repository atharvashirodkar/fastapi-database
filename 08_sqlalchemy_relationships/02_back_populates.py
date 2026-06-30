from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    # Student -> many marks
    marks = relationship("Mark", back_populates="student")


class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    marks = Column(Integer)

    # Mark -> one student
    student = relationship("Student", back_populates="marks")

# Back-populates is used to establish a bidirectional relationship between the Student and Mark classes.
# This allows us to navigate from a Student object to its associated Mark objects and vice versa.
# example:
# student = Student(name="Rahul", age=20)
# mark = Mark(student=student, marks=85)

# note:
# This file defines the relationship structure only.
# It does not create the actual database table until create_all() is called.
print("Back-populates relationship created successfully.")