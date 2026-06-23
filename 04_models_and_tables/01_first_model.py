from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

# Every SQLAlchemy model inherits from Base
# Base class for all database models
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


print("Student model created successfully.")
