# Flask app.py

from flask import Flask
from app.models.todo import db
from config import Config
from app.routes.todo_routes import todo_bp

app = Flask(__name__)

# Apply the configuration
app.config.from_object(Config)
db.init_app(app)  # Initialize the db with the app

# Register the blueprint
app.register_blueprint(todo_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
