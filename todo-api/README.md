# 📝 Flask To-Do API

This is a simple To-Do API built using **Flask** and **SQLite**. It allows users to **Create, Read, Update, and Delete (CRUD)** tasks.

---

## 📌 Features
- 🟢 Add new tasks
- 🔄 Update existing tasks
- ❌ Delete tasks
- 📋 Retrieve all tasks
- 🚀 Built with **Flask & SQLAlchemy**
- 🛠 Error handling for invalid requests

---

## 🛠 Setup Instructions

### 🔹 **1. Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/todo-api.git
cd todo-api

🔹 2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

🔹 3. Install Dependencies

pip install -r requirements.txt

🔹 4. Run the API

python app.py


---

🚀 API Endpoints

 Get All Tasks

Endpoint: GET /tasks

Response:


{
  "tasks": [
    {"id": 1, "title": "Sample Task", "completed": false}
  ]
}

 Add a New Task

Endpoint: POST /tasks

Request Body:


{
  "title": "Buy groceries"
}

Response:


{
  "message": "Task added successfully",
  "task": {"id": 1, "title": "Buy groceries", "completed": false}
}

 Update a Task

Endpoint: PUT /tasks/{task_id}

Request Body:


{
  "title": "Buy milk",
  "completed": true
}

 Delete a Task

Endpoint: DELETE /tasks/{task_id}

Response:


{
  "message": "Task deleted successfully"
}


---

🛠 Technologies Used

Python

Flask

SQLite

SQLAlchemy



---

📌 Future Improvements

✅ Add user authentication

✅ Deploy to a cloud platform



---

🤝 Contributing

Want to contribute? Feel free to submit a pull request!


---

📜 License

This project is MIT Licensed.

