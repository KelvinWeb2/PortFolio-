from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Task Manager API!"})

if __name__ == '__main__':
    app.run(debug=True)
