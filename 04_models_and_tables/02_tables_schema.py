from sqlalchemy import Column, Integer, String
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


print("Table schema defined successfully.")