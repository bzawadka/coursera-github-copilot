from app.models.todo import db, Todo

def add_todo(title):
    """Add a new todo item."""
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()

def update_todo(todo_id):
    """Toggle the completion status of a todo item."""
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        todo.complete = not todo.complete
        db.session.commit()

def delete_todo(todo_id):
    """Delete a todo item."""
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()

def get_all_todos():
    """Retrieve all todo items."""
    return Todo.query.all()