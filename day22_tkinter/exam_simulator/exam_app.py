import tkinter as tk

from day22_tkinter.exam_simulator.exam_service import ExamService

window = tk.Tk()
exam_service = ExamService()
check_a = tk.StringVar(window)
check_b = tk.StringVar(window)
check_c = tk.StringVar(window)
check_d = tk.StringVar(window)
questions = exam_service.get_random_questions()
answers = []
window.title("Exam")
# check_a = tk.Checkbutton(window, text=f"a: {questions[0].a}").pack(fill=tk.X)
# check_b = tk.Checkbutton(window, text=f"b: {questions[0].b}").pack(fill=tk.X)
# check_c = tk.Checkbutton(window, text=f"c: {questions[0].c}").pack(fill=tk.X)
# check_d = tk.Checkbutton(window, text=f"d: {questions[0].d}").pack(fill=tk.X)
# check_a.pack(fill=tk.X)
# check_b.pack(fill=tk.X)
# check_c.pack(fill=tk.X)
# check_d.pack(fill=tk.X)

question_index = 0


def next_click():
    global question_index
    answers.append(f"{check_a.get()}{check_b.get()}{check_c.get()}{check_d.get()}")
    question_index = question_index + 1
    if question_index < len(questions):
        make_window(question_index, questions[question_index], next_click, previous_click,
                    answers[question_index] if len(answers) > question_index else None)
        pre_button.pack()
    else:
        window.destroy()
        print(exam_service.get_score(questions, answers))


def previous_click():
    global question_index
    answers.append(f"{check_a.get()}{check_b.get()}{check_c.get()}{check_d.get()}")
    question_index = question_index - 1
    if question_index == 0:
        pre_button.pack_forget()
    make_window(question_index, questions[question_index], next_click, previous_click,
                answers[question_index] if len(answers) > question_index else None)




def make_window(q_index, question, next_click, previous_click, answer=None):
    q.configure(text=f"Q{q_index + 1}: {question.question}")
    a.configure(text=f"a: {question.a}")
    b.configure(text=f"b: {question.b}")
    c.configure(text=f"c: {question.c}")
    d.configure(text=f"d: {question.d}")
    if answer:
        if 'a' in answer:
            a.select()
        else:
            a.deselect()
        if 'b' in answer:
            b.select()
        else:
            b.deselect()
        if 'c' in answer:
            c.select()
        else:
            c.deselect()
        if 'd' in answer:
            d.select()
        else:
            d.deselect()
    else:
        a.deselect()
        b.deselect()
        c.deselect()
        d.deselect()


question = questions[0]
q = tk.Label(window, text=f"Q1: {question.question}")
q.pack(fill=tk.X)

a = tk.Checkbutton(window, text=f"a: {question.a}", variable=check_a, onvalue='a', offvalue='')
a.pack(fill=tk.X)
b = tk.Checkbutton(window, text=f"b: {question.b}", variable=check_b, onvalue='b', offvalue='')
b.pack(fill=tk.X)
c = tk.Checkbutton(window, text=f"c: {question.c}", variable=check_c, onvalue='c', offvalue='')
c.pack(fill=tk.X)
d = tk.Checkbutton(window, text=f"d: {question.d}", variable=check_d, onvalue='d', offvalue='')
d.pack(fill=tk.X)

next_button = tk.Button(window, text='Next', command=next_click)
next_button.pack()

pre_button = tk.Button(window, text='Previous', command=previous_click)
# pre_button.pack()

# make_window(0, questions[0], next_click, previous_click, answer=None)
window.mainloop()
