class Question:
    def __init__(self, q_id=None, question=None, a=None, b=None, c=None, d=None, answer=None, is_mcq=None) -> None:
        self.q_id = q_id
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.answer = set(answer)
        self.is_mcq = is_mcq
