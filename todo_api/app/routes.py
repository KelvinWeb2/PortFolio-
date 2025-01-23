from flask import Flask, jsonify
from app.models import todos, Todo

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def get_todos():
    """Retrieve all todos"""
    return jsonify([todo.to_dict() for todo in todos]), 200
