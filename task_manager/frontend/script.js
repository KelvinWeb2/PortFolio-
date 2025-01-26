const loginBtn = document.getElementById("login-btn");
const addTaskBtn = document.getElementById("add-task-btn");
const taskList = document.getElementById("tasks");

loginBtn.addEventListener("click", async () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    });

    if (response.ok) {
        const data = await response.json();
        console.log('Login successful', data);
        // Store token (if using JWT) and enable task management
        loadTasks();
    } else {
        alert('Login failed');
    }
});

addTaskBtn.addEventListener("click", async () => {
    const title = document.getElementById("task-title").value;
    const description = document.getElementById("task-desc").value;

    const response = await fetch('http://127.0.0.1:5000/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description })
    });

    if (response.ok) {
        alert('Task added');
        loadTasks();
    } else {
        alert('Failed to add task');
    }
});

async function loadTasks() {
    const response = await fetch('http://127.0.0.1:5000/tasks');
    const tasks = await response.json();
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const taskItem = document.createElement('li');
        taskItem.textContent = `${task.title} - ${task.description}`;
        taskList.appendChild(taskItem);
    });
}
