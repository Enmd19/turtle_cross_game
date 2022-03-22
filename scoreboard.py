from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 265)
        self.write(f"Level: {self.player_score}", align="center", font=FONT)

    def add_point(self):
        self.player_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("Game Over.", align="center", font=FONT)
