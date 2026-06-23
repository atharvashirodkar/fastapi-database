from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

# Every SQLAlchemy model inherits from Base
Base = declarative_base()


# Model representing the students table
class Student(Base):
    # Name of the table inside the database
    __tablename__ = "students"

    # Unique identifier for each student
    id = Column(Integer, primary_key=True)

    # Student name column
    name = Column(String)

    # Student age column
    age = Column(Integer)


# Model representing the courses table
class Course(Base):
    # Name of the table inside the database
    __tablename__ = "courses"

    # Unique identifier for each course
    id = Column(Integer, primary_key=True)

    # Course name column
    name = Column(String)


# Model representing the marks table
class Mark(Base):
    # Name of the table inside the database
    __tablename__ = "marks"

    # Unique identifier for each mark record
    id = Column(Integer, primary_key=True)

    # References a student
    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    # References a course
    course_id = Column(
        Integer,
        ForeignKey("courses.id")
    )

    # Marks obtained by the student
    marks = Column(Integer)


print("Multiple models defined successfully.")