import tkinter as tk
import html
from quiz_brain import QuizBrain
from tkinter.constants import E

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.brain = quiz_brain

        self.window = tk.Tk()
        self.window.title('Quizz App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(False, False)

        self.l_score = tk.Label(text=f"Score: 0", bg=THEME_COLOR, fg='white', font=('Arial', 14))
        self.l_score.grid(row=0, column=1, padx=(0,15), sticky = E)

        self.question_card = tk.Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.question_card.create_text(150, 100, text='Lopos folows aoijdak hshdim qjdokc', width=250, font=('Arial', 16, 'italic'))
        self.question_card.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_img = tk.PhotoImage(file='./images/true.png')
        self.true_bnt = tk.Button(image=true_img, border=0, command=self.press_true)
        self.true_bnt.grid(row=2, column=0, padx=(0,10))

        false_img = tk.PhotoImage(file='./images/false.png')
        self.false_bnt = tk.Button(image=false_img, border=0, command=self.press_false)
        self.false_bnt.grid(row=2, column=1, padx=(10,0))

        self.get_next_question()

        self.window.mainloop()

    def press_true(self):
        self.give_feedback(self.brain.check_answer('true'))

    def press_false(self):
        self.give_feedback(self.brain.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.question_card.config(bg='green')
        else:
            self.question_card.config(bg='red')
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.question_card.config(bg='white')
        print(self.brain.still_has_questions())
        if self.brain.still_has_questions():
            self.update_score()
            q_text = self.brain.next_question()
            self.question_card.itemconfig(self.question_text, text=html.unescape(q_text))
        else:
            self.question_card.itemconfig(self.question_text, text='No more questions.')
            self.true_bnt.config(state='disable')
            self.false_bnt.config(state='disable')

    def update_score(self):
        self.l_score['text'] = f"Score: {self.brain.get_score()}"