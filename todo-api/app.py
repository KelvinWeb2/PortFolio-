from flask import Flask, jsonify, request
from models.models import db, Task
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Ensure tables are created
with app.app_context():
    db.create_all()

# Handle invalid JSON errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request – Invalid JSON format'}), 400

# Handle missing resources
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify({'tasks': [task.to_dict() for task in tasks]})

# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    try:
        data = request.get_json()
        if not data or 'title' not in data:
            return jsonify({'error': 'Task title is required'}), 400

        task = Task(title=data['title'])
        db.session.add(task)
        db.session.commit()
        return jsonify({'message': 'Task added successfully', 'task': task.to_dict()}), 201
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON format'}), 400

# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    try:
        data = request.get_json()
        if 'title' in data:
            task.title = data['title']
        if 'completed' in data:
            task.completed = data['completed']

        db.session.commit()
        return jsonify({'message': 'Task updated successfully', 'task': task.to_dict()})
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON format'}), 400

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
