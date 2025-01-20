''' from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)  '''

from flask import Flask, render_template, request

app = Flask(__name__)

# Sample questions
questions = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "id": 2,
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]

@app.route("/")
def index():
    return render_template("index.html", questions=questions)

@app.route("/result", methods=["POST"])
def result():
    user_answers = request.form
    score = 0
    for question in questions:
        user_answer = user_answers.get(f"question{question['id']}")
        if user_answer == question["answer"]:
            score += 1
    return render_template("result.html", score=score, total=len(questions))

if __name__ == "__main__":
    app.run(debug=True)
