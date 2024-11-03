from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

quiz_data = [
    {
        'question': "What is the capital of France?",
        'options': ['Berlin', 'Madrid', 'Paris', 'Lisbon'],
        'answer': 'Paris'
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Mars'
    },
    {
        'question': "Who wrote 'Hamlet'?",
        'options': ['Charles Dickens', 'Jane Austen', 'William Shakespeare', 'Mark Twain'],
        'answer': 'William Shakespeare'
    }
]

@app.route('/')
def quiz():
    return render_template('quiz.html', quiz_data=quiz_data)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for index, question in enumerate(quiz_data):
        selected_answer = request.form.get(f'question{index}')
        if selected_answer == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(quiz_data))

if __name__ == '__main__':
    app.run(debug=True)
