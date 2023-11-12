import tkinter as tk
from tkinter import messagebox
import time

questions = [
    {
        'question': 'Какой язык программирования используется для научных вычислений?',
        'options': ['Python', 'R', 'JavaScript', 'Swift'],
        'answer': 'Python',
        'time': 0
    },
    {
        'question': 'Какой язык программирования часто используется для написания операционных систем?',
        'options': ['Python', 'C', 'JavaScript', 'Java'],
        'answer': 'C',
        'time': 0
    },
    {
        'question': 'Какой язык программирования используется для разработки приложений на Android?',
        'options': ['Swift', 'Kotlin', 'C#', 'Java'],
        'answer': 'Kotlin',
        'time': 0
    },
    {
        'question': 'С помощью какого языка программирования можно разрабатывать системы искусственного интеллекта?',
        'options': ['JavaScript', 'PHP', 'Python', 'Java'],
        'answer': 'Python',
        'time': 0
    },
    {
        'question': 'Какой язык программирования часто используется для веб-разработки на сервере?',
        'options': ['Python', 'JavaScript', 'PHP', 'Swift'],
        'answer': 'PHP',
        'time': 0
    },
    {
        'question': 'Какой язык программирования лучше всего использовать для веб-разработки?',
        'options': ['JavaScript', 'Python', 'Java', 'C#'],
        'answer': 'JavaScript',
        'time': 0
    },
    {
        'question': 'Какой язык программирования используется для мобильной разработки?',
        'options': ['Java', 'Swift', 'Kotlin', 'Objective-C'],
        'answer': 'Swift',
        'time': 0
    },
    {
        'question': 'Какой язык программирования используется для разработки приложений для Windows?',
        'options': ['C#', 'Java', 'Python', 'C'],
        'answer': 'C#',
        'time': 0
    }
]


class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.index = -1

        self.score = 0
        self.start_time = time.time()
        self.quiz_start_time = time.time()
        self.correct_answers = []

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.quit_button = tk.Button(self.frame, text='Закончить викторину', command=self.quit)
        self.quit_button.pack(side='bottom')

        self.question_label = tk.Label(self.frame)
        self.question_label.pack(side='top')

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(self.frame, textvariable=self.answer_var)
        self.answer_entry.pack(side='top')

        self.submit_button = tk.Button(self.frame, text='Отправить ответ', command=self.submit)
        self.submit_button.pack(side='bottom')

        self.show_next_question()


    def show_next_question(self):
        self.index += 1
        if self.index < len(self.questions):
            q = self.questions[self.index]['question']
            self.question_label['text'] = f'Вопрос #{self.index + 1}:\n{q}\n\nВремя, потраченное на предыдущий вопрос: неизвестно.'
            self.start_time = time.time()
            self.answer_entry.focus_set()
        else:
            self.end_quiz()

    def submit(self):
        answer = self.answer_var.get().strip()
        if not answer:
            messagebox.showinfo('Внимание', 'Введите свой ответ.')
        else:
            self.questions[self.index]['time'] = int(time.time() - self.start_time)
            if answer == self.questions[self.index]['answer']:
                data = f"Вопрос #{self.index + 1} ({self.questions[self.index]['question']}): правильный ответ '{answer}'"
                self.correct_answers.append(data)
                self.score += 1
            self.answer_var.set('')
            self.show_next_question()
    def quit(self):
        confirm = messagebox.askyesno('Вы уверены?', 'Вы действительно хотите завершить викторину?')
        if confirm:
            self.questions[self.index]['time'] = int(time.time() - self.start_time)  # Добавьте вычисление времени здесь также
            self.end_quiz()

    def end_quiz(self):
        self.quiz_end_time = time.time()

        elapsed_time = int(self.quiz_end_time - self.quiz_start_time)
        self.question_label[
            'text'] = f'Конец викторины! Ваш итоговый результат: {self.score}/{len(self.questions)}. \n\nОбщее время: {elapsed_time} секунд.\n\nВремя на каждый вопрос:'
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.quit_button.pack_forget()
        for i, question in enumerate(self.questions, 1):
            q = question['question']
            t = question['time'] if question['time'] > 0 else "Не подчитано"
            self.question_label['text'] += f'\n\nВопрос #{i}: {q}\nВремя: {t}'

        self.question_label['text'] += '\n\nУ вас были следующие верные ответы:\n'
        for answer in self.correct_answers:
            self.question_label['text'] += answer + "\n"


root = tk.Tk()
app = QuizApp(root, questions)
root.mainloop()