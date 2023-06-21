from tkinter import *
import time

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzle")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Score
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        # True Button
        self.true = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true, bg=THEME_COLOR, highlightthickness=0, command=self.click_true)
        self.true_button.grid(column=0, row=2)

        # False Button
        self.false = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false, bg=THEME_COLOR, highlightthickness=0, command=self.click_false)
        self.false_button.grid(column=1, row=2)

        # Question Text
        self.q_text = self.canvas.create_text(150, 125, width=280, text="?", font=("Arial", 20, "italic"))
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            next_q = self.quiz.next_question()
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.q_text, text=next_q)
        else:
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.q_text, text="Congratulations! You finished the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def click_true(self):
        feedback = self.quiz.check_answer("True")
        self.give_feedback(feedback)

    def click_false(self):
        feedback = self.quiz.check_answer("False")
        self.give_feedback(feedback)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            self.update_score()
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

    def update_score(self):
        score = self.quiz.score
        self.score.config(text=f"Score: {score}")



