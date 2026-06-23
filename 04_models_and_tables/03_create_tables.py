from sqlalchemy import Column, Integer, String, create_engine
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


# Create a database engine
engine = create_engine(
    "sqlite:///students.db"
)

# Create all tables defined using Base
Base.metadata.create_all(engine)

print("Table created successfully.")

from db_table_viewer import view_table_schema

view_table_schema("students")