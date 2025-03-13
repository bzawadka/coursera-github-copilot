# Flask app.py

from app import create_app
from app.models.todo import db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
