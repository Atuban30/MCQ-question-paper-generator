# To insert the questions into the Mongodb from Question Bank
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/questionbank"
mongo = PyMongo(app)
CORS(app)

@app.route('/api/questions', methods=['POST'])
def add_question():
    question_data = request.json
    mongo.db.questions.insert_one(question_data)
    return jsonify({"message": "Question added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
