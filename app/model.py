from datetime import datetime
from sqlalchemy.sql import func
from database import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    tags = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())

    answers = db.relationship('Answer', backref='question', lazy=True)

    def __repr__(self):
        return f'<Question {self.id}>'

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)

    def __repr__(self):
        return f'<Answer {self.id}>'
