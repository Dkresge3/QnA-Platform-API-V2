from flask import Blueprint, jsonify, request
from app import db
from app.models import Question, Answer

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    results = []
    for question in questions:
        question_data = {}
        question_data['id'] = question.id
        question_data['title'] = question.title
        question_data['body'] = question.body
        question_data['tags'] = question.tags
        results.append(question_data)
    return jsonify(results)

@bp.route('/questions', methods=['POST'])
def create_question():
    data = request.get_json()
    new_question = Question(
        title=data['title'],
        body=data['body'],
        tags=data['tags']
    )
    db.session.add(new_question)
    db.session.commit()
    return jsonify({'message': 'Question created successfully!'})

@bp.route('/questions/<int:question_id>/answers', methods=['POST'])
def create_answer(question_id):
    data = request.get_json()
    question = Question.query.get(question_id)
    new_answer = Answer(
        answer_text=data['answer_text'],
        question=question
    )
    db.session.add(new_answer)
    db.session.commit()
    return jsonify({'message': 'Answer created successfully!'})
