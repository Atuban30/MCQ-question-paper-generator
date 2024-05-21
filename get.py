# To fetch questions from MongoDB
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/questionbank"
mongo = PyMongo(app)
CORS(app)

@app.route('/api/questions', methods=['GET'])
def get_questions():
    questions = mongo.db.questions.find()
    question_list = []
    for question in questions:
        question_list.append({
            "questionText": question["questionText"],
            "answerOptions": question["answerOptions"],
            "correctAnswer": question["correctAnswer"]
        })
    return jsonify(question_list)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
