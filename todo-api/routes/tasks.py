from flask import Blueprint, jsonify, request

tasks_bp = Blueprint('tasks', __name__)

# Sample in-memory database
tasks = []

# Get all tasks
@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Add a new task
@tasks_bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Task title is required'}), 400

    task = {'id': len(tasks) + 1, 'title': data['title'], 'completed': False}
    tasks.append(task)
    return jsonify({'message': 'Task added successfully', 'task': task}), 201

# Update a task
@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['completed'] = data.get('completed', task['completed'])
            return jsonify({'message': 'Task updated successfully', 'task': task}), 200
    return jsonify({'error': 'Task not found'}), 404

# Delete a task
@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'}), 200

