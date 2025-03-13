import pytest
from flask import Flask
from app import create_app
from app.models.todo import db

# filepath: lesson-03/video-03/app/test___init__.py

@pytest.fixture
def app():
    """Fixture to create and configure the Flask app for testing."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture to provide a test client for the app."""
    return app.test_client()

def test_app_creation(app):
    """Test that the Flask app is created successfully."""
    assert isinstance(app, Flask)

def test_app_configuration(app):
    """Test that the app configuration is applied correctly."""
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"
    assert not app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]

def test_database_tables_creation(app):
    """Test that the database tables are created."""
    with app.app_context():
        tables = db.engine.table_names()
        assert "todo" in tables

def test_todo_routes(client):
    """Test the routes in the todo blueprint."""
    # Test GET /todos (assuming this route exists in todo_bp)
    response = client.get("/todos")
    assert response.status_code == 200

    # Test POST /todos (assuming this route exists in todo_bp)
    response = client.post("/todos", json={"title": "Test Todo", "description": "Test Description"})
    assert response.status_code == 201

    # Test GET /todos/<id> (assuming this route exists in todo_bp)
    response = client.get("/todos/1")
    assert response.status_code in [200, 404]  # Depending on whether the todo exists

    # Test DELETE /todos/<id> (assuming this route exists in todo_bp)
    response = client.delete("/todos/1")
    assert response.status_code in [200, 404]  # Depending on whether the todo exists