from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.available = True
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(150, 125, text='Some long Question',
                                                fill=THEME_COLOR, font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true = PhotoImage(file='images/true.png')
        self.true = Button(image=true, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.true.grid(column=0, row=2)
        false = PhotoImage(file='images/false.png')
        self.false = Button(image=false, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.false.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question, text=question)
            self.available = True
        else:
            score = self.quiz_brain.final_score()
            message = f'You answered all the questions. Your score was {score[0]}/{score[1]}.'
            self.canvas.itemconfig(self.question, text=message)
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def true_pressed(self):
        if self.available:
            self.available = False
            result = self.quiz_brain.check_answer('True')
            self.result(result)

    def false_pressed(self):
        if self.available:
            self.available = False
            result = self.quiz_brain.check_answer('False')
            self.result(result)

    def result(self, correct):
        if correct:
            self.canvas.config(bg='green')
            self.score.config(text=f'Score: {self.quiz_brain.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
