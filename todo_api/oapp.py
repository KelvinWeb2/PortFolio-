from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection helper function
def get_db_connection():
    conn = sqlite3.connect('tasks.db')  # Connect to the SQLite database
    conn.row_factory = sqlite3.Row     # Return rows as dictionaries
    return conn

# Initialize the database
@app.route('/init_db', methods=['GET'])
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    return jsonify({"message": "Database initialized!"})

# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data.get('title'):
        return jsonify({"error": "title is required"}), 400

    title = data['title']
    status = data.get('status', "Incomplete")
    
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (title, status) VALUES (?, ?)', (title, status))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Task added successfully!", "task": {"title": title, "status": status}})

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()

    tasks_list = [{"id": task["id"], "title": task["title"], "status": task["status"]} for task in tasks]
    return jsonify({"tasks": tasks_list})

# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    title = data.get('title')
    status = data.get('status')
    
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET title = ?, status = ? WHERE id = ?', (title, status, task_id))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Task updated successfully!"})

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Task deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
