from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory database
tasks = []

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Task title is required'}), 400

    task = {'id': len(tasks) + 1, 'title': data['title'], 'completed': False}
    tasks.append(task)
    return jsonify({'message': 'Task added successfully', 'task': task}), 201

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
