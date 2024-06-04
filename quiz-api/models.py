class Question:
    def __init__(self, position: int, title: str, text: str, image: str = None):
        self.position = position
        self.title = title
        self.text = text
        self.image = image
