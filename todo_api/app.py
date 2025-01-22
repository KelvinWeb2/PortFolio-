from flask import Flask, request, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Initialize database
def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')

    # Tasks table
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'Incomplete',
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')

    conn.commit()
    conn.close()

# Generate token
def generate_token(user_id):
    s = Serializer(app.config['SECRET_KEY'], expires_in=3600)  # Token expires in 1 hour
    return s.dumps({'user_id': user_id}).decode('utf-8')

# Verify token
def verify_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
        return data['user_id']
    except:
        return None

# User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 400
    finally:
        conn.close()

    return jsonify({'message': 'User registered successfully'}), 201

# User login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        token = generate_token(user[0])
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Protected route (example)
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Token is missing'}), 401

    user_id = verify_token(token)
    if not user_id:
        return jsonify({'error': 'Invalid or expired token'}), 401

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        data = request.json
        title = data.get('title')
        description = data.get('description')

        if not title:
            return jsonify({'error': 'Title is required'}), 400

        cursor.execute('INSERT INTO tasks (title, description, user_id) VALUES (?, ?, ?)', (title, description, user_id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Task created successfully'}), 201

    elif request.method == 'GET':
        cursor.execute('SELECT id, title, description, status FROM tasks WHERE user_id = ?', (user_id,))
        tasks = [{'id': row[0], 'title': row[1], 'description': row[2], 'status': row[3]} for row in cursor.fetchall()]
        conn.close()
        return jsonify({'tasks': tasks}), 200

# Initialize database
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
