from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.responses import JSONResponse
from database import engine
from models import TodoCreate, TodoRead, TodoUpdate, Todo
from typing import List
from fastapi.exceptions import RequestValidationError

app = FastAPI()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


Base.metadata.create_all(bind=engine)
@app.get("/todos/", response_model=List[TodoRead])
def list_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    return [TodoRead(**todo.__dict__) for todo in todos]

@app.post("/todos/", response_model=TodoRead)
def create_todo(todo: TodoCreate):
    db = SessionLocal()
    new_todo = Todo(title=todo.title, description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return TodoRead(**new_todo.__dict__)

@app.get("/todos/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int):
    db = SessionLocal()
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoRead(**todo.__dict__)

@app.put("/todos/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoUpdate):
    db = SessionLocal()
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.title:
        db_todo.title = todo.title
    if todo.description:
        db_todo.description = todo.description
    if todo.completed is not None:
        db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return TodoRead(**db_todo.__dict__)

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    db = SessionLocal()
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}

# Add a general exception handler
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    error_message = "Oop's Something went wrong"
    return JSONResponse(status_code=500, content={"message": error_message})

# Add a request validation exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error_message = "Please Enter valid input"
    return JSONResponse(status_code=400, content={"message": error_message})
