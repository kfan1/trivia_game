from tkinter import *

THEME_COLOR = "#375362"
number = 0
score = 0
pause = ""


class Window(Tk):
    def __init__(self, question_bank):
        super().__init__()
        self.question_bank = question_bank
        self.title('10 Trivia Questions!')
        self.config(background=THEME_COLOR, padx=30, pady=30)
        self.true_image = PhotoImage(file='./images/true.png')
        self.false_image = PhotoImage(file='./images/false.png')
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false)
        self.canvas = Canvas(width=500, height=400, background=THEME_COLOR, highlightthickness=0)
        self.score_board = self.canvas.create_text(250, 20, text=f'Score: {score}', font=('Arial', 26, 'bold'), fill='white')
        self.question_text = self.canvas.create_text(250, 200, width=500, text=f'Q{number+1}. {self.question_bank[number].text}', font=('Arial', 20, 'italic'), fill='white')

        self.canvas.grid(column=0, row=0, columnspan=2)
        self.false_button.grid(column=0, row=1)
        self.true_button.grid(column=1, row=1)

        self.mainloop()

    def nothing(self):
        pass

    def next_question(self):
        global number
        self.false_button.config(command=self.false)
        self.true_button.config(command=self.true)
        number += 1
        if number == len(self.question_bank):
            self.canvas.itemconfig(self.question_text, text=f'Your final score is {score}')
            self.false_button.config(command=self.nothing)
            self.true_button.config(command=self.nothing)
            self.canvas['background'] = THEME_COLOR
            self.quitting()
        else:
            self.canvas['background'] = THEME_COLOR
            self.canvas.itemconfig(self.question_text, text=f'Q{number+1}. {self.question_bank[number].text}')

    def quitting(self):
        self.after(3000, self.quit)

    def true(self):
        global pause, score
        if self.question_bank[number].answer == 'False':
            self.canvas['background'] = 'red'
            self.false_button.config(command=self.skip_waiting)
            self.true_button.config(command=self.skip_waiting)
            pause = self.after(3000, self.next_question)
        else:
            score += 1
            self.canvas.itemconfig(self.score_board, text=f'Score: {score}')
            self.next_question()

    def false(self):
        global pause, score
        if self.question_bank[number].answer == 'True':
            self.canvas['background'] = 'red'
            self.false_button.config(command=self.skip_waiting)
            self.true_button.config(command=self.skip_waiting)
            pause = self.after(3000, self.next_question)
        else:
            score += 1
            self.canvas.itemconfig(self.score_board, text=f'Score: {score}')
            self.next_question()

    def skip_waiting(self):
        global pause
        self.after_cancel(pause)
        self.next_question()



