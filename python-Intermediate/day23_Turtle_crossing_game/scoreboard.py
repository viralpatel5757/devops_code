from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard (Turtle):

    def __init__(self) :
       super().__init__()
       self.hideturtle()
       self.score = 1
       self.update_scoreboard()

    def update_scoreboard(self):
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()    

    def game_over(self):
        self.penup()
        self.goto(0,0)  
        self.write("GAME OVER", align="center", font=FONT) 
