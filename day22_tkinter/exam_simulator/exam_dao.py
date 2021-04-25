import pymysql
from pymysql.cursors import DictCursor

from day22_tkinter.exam_simulator.question_model import Question


class ExamDao:
    QUESTIONS_TABLE = 'questions'
    GET_QUESTION = "Select * from questions where q_id = %s"
    GET_QUESTION_IDS = "Select q_id from questions"
    ADD_QUESTION = "insert into questions(question, a,b,c,d,answer,is_mcq) values(%s, %s, %s, %s, %s, %s, %s);"

    def __init__(self):
        self.conn = pymysql.connect(user='root', password="root", host='localhost', database='exam')

    def get_question(self, q_id) -> Question:
        cursor = self.conn.cursor(cursor=DictCursor)
        cursor.execute(self.GET_QUESTION, (q_id,))
        return Question(**cursor.fetchone())

    def add_question(self, question: Question):
        cursor = self.conn.cursor()
        cursor.execute(self.ADD_QUESTION, (question.question, question.a,
                                           question.b, question.c, question.d, ''.join(question.answer), question.is_mcq))
        # cursor.commit()
        return cursor.fetchone()

    def get_all_question_ids(self):
        cursor = self.conn.cursor()
        cursor.execute(self.GET_QUESTION_IDS)
        return cursor.fetchall()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    exam_dao = ExamDao()
    exam_dao.add_question(
        Question(question="What is Jaipur also called?", a='Blue city', b='Golden city', c='Pink city',
                 d='None of the above', answer='c', is_mcq=0))
