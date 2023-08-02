from fastapi import FastAPI, Path
from pydantic import BaseModel

# to run on the browser "uvicorn main:app --reload"
app = FastAPI()
students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "12"
    },
    2: {
        "name": "jo",
        "age": 18,
        "year": "13"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: str | None = None
    age: int | None = None
    year: str | None = None


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="the Id of the student you want to view", gt=0, le=4)):
    return students[student_id]


# http://127.0.0.1:8000/get-student/2(student id)

@app.get("/search_std/{test}")
def read_items(name: str | None = None, *, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]["age"], test
    return {"data": "not found"}


# http://127.0.0.1:8000/items?name=jo(student name)
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error", "Student exists"}
    students[student_id] = student
    return students[student_id]


# http://127.0.0.1:8000/create-student/3

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Student doesn't exist"}
    if student.name is not None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]["age"] = student.age
    if student.year is not None:
        students[student_id]["year"] = student.year
    return students[student_id]


# http://127.0.0.1:8000/update-student/2

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student doesn't exist"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}
# http://127.0.0.1:8000/delete-student/1
