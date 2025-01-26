from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# In-memory database for users and tasks
users = []
tasks = []

# Register route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    for user in users:
        if user['username'] == username:
            return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    users.append({"username": username, "password": hashed_password})

    return jsonify({"message": "User registered successfully"}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    for user in users:
        if user['username'] == username:
            if check_password_hash(user['password'], password):
                return jsonify({"message": "Login successful"}), 200
            else:
                return jsonify({"error": "Invalid password"}), 401

    return jsonify({"error": "User not found"}), 404

# Create a task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400

    task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'done': False
    }
    tasks.append(task)

    return jsonify({"message": "Task created successfully", "task": task}), 201

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks}), 200

# Update a task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    task['done'] = data.get('done', task['done'])

    return jsonify({"message": "Task updated successfully", "task": task}), 200

# Delete a task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = next((task for task in tasks if task['id'] == id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)

    return jsonify({"message": "Task deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
