from flask import Flask, jsonify, request
from app import db
from app.models import Question, Quiz, QuizQuestion

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

# Define your API routes here.
