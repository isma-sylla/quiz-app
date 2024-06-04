from models import Question

def question_to_dict(question: Question) -> dict:
    return {
        "position": question.position,
        "title": question.title,
        "text": question.text,
        "image": question.image
    }

def dict_to_question(data: dict) -> Question:
    return Question(
        position=data['position'],
        title=data['title'],
        text=data['text'],
        image=data.get('image')
    )
