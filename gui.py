from tkinter import *

class QuizGUI:
    def __init__(self, quizMethods):
        #call the quizMethods class to use the methods
        self.quizMethods = quizMethods
        self.screen = Tk()

        #set question counter
        self.counter =0

        self.screen.title("Boolean Quiz")
        self.screen.minsize(300, 400)
        self.screen.config(bg="navy")

        #set the question screen)
        self.game_screen = Canvas(width=250, height=250, bg="black")
        self.qDisplay = self.game_screen.create_text(130, 120, width=170, text="q text", fill="yellow",font=("Ariel", 14, "bold", "italic"))
        self.game_screen.place(x=25, y=10)

        # add gameboard design to lower screen
        self.desDisplay = Canvas(width=192, height=115, bd=0, highlightthickness=0)
        design_img = PhotoImage(file="images/arcade.png")
        self.display = self.desDisplay.create_image(96, 57, image=design_img)
        self.desDisplay.place(x=52, y=270)

        # create True/False buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true = Button(image=true_img, highlightthickness=0, borderwidth=1, bg="navy", relief="ridge",
                           command=self.true_button)
        self.false = Button(image=false_img, highlightthickness=0, borderwidth=1, relief="ridge", bg="navy",
                            command=self.false_button)
        self.true.place(x=20, y=280)
        self.false.place(x=210, y=280)

        # create the timer display
        self.timer = Canvas(bg="black", width=60, height=30)
        self.timer_txt = self.timer.create_text(33, 15, text="00:00", font=("Arial", 15), fill="white")
        self.timer.pack()
        # call the countdown function to start count down
        self.countdown(secs=120)


       # create the score keeper
        self.scoreScreen = Canvas(bg="navy", width=100, height=60, bd=0, highlightthickness=0)
        self.score_txt = self.scoreScreen.create_text(45, 20, text="Score: 0", font=("Arial", 12), fill="white")
        self.scoreScreen.place(x=105, y=300)

        #call to change q and update score
        self.change_q()

        #for keeping the game on
        self.screen.mainloop()

    #changes question/updates score
    def change_q(self):
        self.counter+=1
        self.game_screen.config(bg="black")

        #gets a new question via new_q method from qM class and displays on screen
        self.update_text = self.quizMethods.new_q()
        self.game_screen.itemconfig(self.qDisplay, text=self.update_text)

        #updates the score board everytime qestion is correct
        self.game_score = self.quizMethods.score_track()
        self.scoreScreen.itemconfig(self.score_txt, text=f"Score: {self.game_score}/20")

        #ends gaem after all questions have been answered
        if self.counter==20:
            self.clear_screen()


    #gives true button fnctionality
    def true_button(self):
        validate = self.quizMethods.verify_answ("True")
        self.feedback(validate)

    #gives false button functionality
    def false_button(self):
        validate = self.quizMethods.verify_answ("False")
        self.feedback(validate)

    #gives user feedback on answer by turning screen green or red
    def feedback(self, validate):
        if validate is True:
            self.game_screen.config(bg="green")
        else:
            self.game_screen.config(bg="red")

        self.screen.after(1000, self.change_q)

    #makes the timer function
    def countdown(self, secs):
        mins = secs // 60
        secs_left = secs % 60

        #clear screen if time is up
        if secs==0:
            self.clear_screen()

        #format seconds when they are less than 10
        if secs_left < 10:
            secs_left = f"0{secs_left}"

        #format mins
        if mins < 10:
            mins = f"0{mins}"

        #subtracts 1 from the seconds every second
        if secs > 0:
            self.screen.after(1000, self.countdown, secs - 1)

        #turn the bg red for 10 sec warning
        if secs<10:
            self.timer.config(bg="red")

        #updates the timer canvas to display the countdown
        self.timer.itemconfig(self.timer_txt, text=f"{mins}:{secs_left}")

    #disables buttons, returns score on screen
    def clear_screen(self):
        self.true.config(state=DISABLED)
        self.false.config(state=DISABLED)
        self.timer.destroy()
        self.game_screen.itemconfig(self.qDisplay, text=f"GAME OVER\nSCORE: {self.game_score}/20")


