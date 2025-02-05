from flask import Flask, jsonify, request
from models.models import db, Task

app = Flask(__name__)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db.init_app(app)

with app.app_context():
    db.create_all()  # Create tables if they don't exist

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify({"tasks": [task.to_dict() for task in tasks]})

# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Task title is required"}), 400

    task = Task(title=data["title"])
    db.session.add(task)
    db.session.commit()
    
    return jsonify({"message": "Task added successfully", "task": task.to_dict()}), 201

if __name__ == '__main__':
    app.run(debug=True)
