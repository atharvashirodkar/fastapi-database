from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    age: int


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int


class CourseCreate(BaseModel):
    name: str


class CourseResponse(BaseModel):
    id: int
    name: str


class MarkCreate(BaseModel):
    student_id: int
    course_id: int
    marks: int


class MarkResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    marks: int
