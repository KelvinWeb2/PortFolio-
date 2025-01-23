from flask import Flask, request, jsonify
from .models import todos, Todo

app = Flask(__name__)

# GET /todos - Retrieve all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify([todo.to_dict() for todo in todos]), 200

# POST /todos - Add a new todo
@app.route('/todos', methods=['POST'])
def add_todo():
    # Get JSON data from the request
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    # Validate input
    if not title:
        return jsonify({"error": "Title is required"}), 400

    # Create a new todo
    new_todo = Todo(title, description)
    new_todo.id = len(todos) + 1  # Assign a unique ID
    todos.append(new_todo)  # Add to the in-memory list

    # Return the new todo as a response
    return jsonify(new_todo.to_dict()), 201
