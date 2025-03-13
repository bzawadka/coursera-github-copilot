# Flask app.py

from flask import Flask, render_template, request, redirect, url_for
from models.todo import db
from config import Config
from services.services import add_todo, update_todo, delete_todo, get_all_todos

app = Flask(__name__)

# Apply the configuration
app.config.from_object(Config)
db.init_app(app)  # Initialize the db with the app


# route to add a new todo
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    add_todo(title)
    return redirect(url_for('index'))


# route to update a todo
@app.route('/update/<int:todo_id>')
def update(todo_id):
    update_todo(todo_id)
    return redirect(url_for('index'))


# route to delete a todo
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    delete_todo(todo_id)
    return redirect(url_for('index'))


@app.route('/')
def index():
    todo_list = get_all_todos()
    return render_template('base.html', todo_list=todo_list)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
