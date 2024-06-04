from flask import Flask, request
from flask_cors import CORS
import hashlib
from jwt_utils import build_token, decode_token
from models import Question
from crud import create_question
from serializers import dict_to_question
import database

app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200


@app.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	tried_password = payload['password'].encode('UTF-8')
	hashed = hashlib.md5(tried_password).digest()
	token = build_token()
	if hashed == b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
		return {'token' : token}, 200
	else:
		return {"error": "Unauthorized"}, 401

@app.route('/questions', methods=['POST'])
def post_question():
    token = request.headers.get('Authorization')
    if not token:
        return {"error": "Authorization token is missing"}, 400

    payload = request.get_json()
    question = dict_to_question(payload)
    
    create_question(question)
    
    return {"message": "Question added successfully"}, 200

@app.route('/rebuild-db', methods=['POST'])
def rebuild_db():
    token = request.headers.get('Authorization')
    if not token:
        return {"error": "Authorization token is missing"}, 400

    try:
        # Décodez et vérifiez le token
        decode_token(token)
    except Exception as e:
        return {"error": "Unauthorized"}, 401
    
    # Réinitialisez la base de données
    database.init_db()
    return {"message": "Database rebuilt successfully"}, 200

if __name__ == "__main__":
    app.run()