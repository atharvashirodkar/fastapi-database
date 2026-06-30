from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    age = Column(Integer)

    marks = relationship("Mark")


class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("students.id"))

    marks = Column(Integer)


# This file defines the relationship structure only.
# It does not create the actual database table until create_all() is called.
print("First relationship created successfully.")
