from flask import Blueprint, render_template, request, redirect, url_for
from app.services.services import add_todo, update_todo, delete_todo, get_all_todos

todo_bp = Blueprint('todo', __name__)  # Create a blueprint


# Route to add a new todo
@todo_bp.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    add_todo(title)
    return redirect(url_for('todo.index'))


# Route to update a todo
@todo_bp.route('/update/<int:todo_id>')
def update(todo_id):
    update_todo(todo_id)
    return redirect(url_for('todo.index'))


# Route to delete a todo
@todo_bp.route('/delete/<int:todo_id>')
def delete(todo_id):
    delete_todo(todo_id)
    return redirect(url_for('todo.index'))


# Route to display the index page
@todo_bp.route('/')
def index():
    todo_list = get_all_todos()
    return render_template('base.html', todo_list=todo_list)