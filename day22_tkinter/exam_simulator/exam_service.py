import random
from typing import List

from day22_tkinter.exam_simulator.exam_dao import ExamDao
from day22_tkinter.exam_simulator.question_model import Question


class ExamService:
    def __init__(self):
        self.exam_dao = ExamDao()

    def get_random_questions(self, no = 5):
        all_question_ids = self.exam_dao.get_all_question_ids()

        if len(all_question_ids) > no:
            randon_question_ids = {}
            while len(randon_question_ids) < 5:
                randon_question_ids.update(random.choice(list))
        else:
            randon_question_ids = set(all_question_ids)

        return [self.exam_dao.get_question(q_id) for q_id in randon_question_ids]

    @staticmethod
    def get_score(questions: List[Question], answers: list):
        score = 0
        for i in range(len(questions)):
            if questions[i].answer == set(answers[i]):
                score += 1
        return score

