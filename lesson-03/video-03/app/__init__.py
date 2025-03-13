from flask import Flask
from app.models.todo import db
from config import Config
from app.routes.todo_routes import todo_bp

def create_app() -> Flask:
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__, template_folder='templates')

    # Apply the configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables

    # Register blueprints
    app.register_blueprint(todo_bp)

    return app