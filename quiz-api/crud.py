import sqlite3
from models import Question

DATABASE_PATH = './quiz.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_question(question: Question):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO questions (position, title, text, image)
        VALUES (?, ?, ?, ?)
    ''', (question.position, question.title, question.text, question.image))
    conn.commit()
    conn.close()

def get_question_by_position(position: int) -> Question:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questions WHERE position = ?', (position,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Question(row['position'], row['title'], row['text'], row['image'])
    return None
