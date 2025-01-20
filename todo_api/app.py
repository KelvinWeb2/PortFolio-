from flask import Flask

app = Flask(__name__)  # Create an instance of Flask

@app.route("/")  # This defines the homepage URL
def home():
    return {"message": "Welcome to the To-Do List API"}

if __name__ == "__main__":
    app.run(debug=True)  # Runs the app in debug mode
