from fastapi import FastAPI
from random import randrange
from pydantic import BaseModel

app = FastAPI()

todo_items = []

class TodoCreate(BaseModel):
    task: str
    description: str
    summary: str
    completed: bool

@app.get("/")
async def root():
    return {"message": "Todo API"}

@app.get("/todos")
def get_todos():
    return {"data": todo_items}

@app.post("/todos")
def add_todo(todo: TodoCreate):
    todo_dict = todo.dict()
    todo_dict['id'] = randrange(0, 1000)
    todo_items.append(todo_dict)
    return {"data": todo_dict}


def get_id(id):
    for i in todo_items:
        if i["id"] == id:
            return i
    

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    post = get_id(todo_id)
    return post



def todo_index(id):
    for i, p in enumerate(todo_items):
         if p["id"] == id:
            return i

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    post = todo_index(todo_id)
    todo_items.pop(post)
    return post


@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo:TodoCreate):
    todo_index = todo_index(todo_id)
    if todo_index is not None:
        todo_item = todo_items[todo_index]
        todo_item.task = updated_todo.task
        todo_item.description = updated_todo.description
        todo_item.summary = updated_todo.summary
        todo_item.completed = updated_todo.completed
        return {"message": "Todo item updated successfully"}
    return {"message": "Todo item not found"}
    