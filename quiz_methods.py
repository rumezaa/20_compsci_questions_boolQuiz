import html
class Quizsetup:
    def __init__(self,data):
        self.data = data
        self.score = 0
        self.current_q=0

    def new_q(self):
        #index the q_list to get the question
        self.next_question = self.data[self.current_q]
        self.current_q += 1

        #format question into natural language
        self.format_q = html.unescape("".join(map(str, list(self.next_question.keys()))))

        return self.format_q

    #returns True if answer is correct, false if its wrong
    def verify_answ(self,input):
        self.input = input
        self.answer = "".join(map(str, list(self.next_question.values())))

        if self.input == self.answer:
            self.score+=1
            return True
        else:
            return False

    #returns user score
    def score_track(self):
        return f"{self.score}"

















