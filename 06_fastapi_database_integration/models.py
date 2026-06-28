from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    age = Column(Integer)