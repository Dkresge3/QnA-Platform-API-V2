from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
# from model import Question, Quiz, QuizQuestion
from database import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
CORS(app)
db.init_app(app)

# ... Define your API routes here ...
