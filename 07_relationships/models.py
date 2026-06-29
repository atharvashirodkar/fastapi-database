from sqlalchemy import Column, Integer, String, ForeignKey
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


class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("students.id"))

    course_id = Column(Integer, ForeignKey("courses.id"))

    marks = Column(Integer)
