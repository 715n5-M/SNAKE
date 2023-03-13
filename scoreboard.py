from turtle import Turtle
import random


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/05mon/Desktop/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.ht()
        self.update_s()

    def update_s(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Times", 20, "normal"))

    def increase(self):
        self.score += 1
        self.update_s()

    def reset_s(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/05mon/Desktop/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_s()

    def eat(self):
        self.clear()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.write("nom, nom, nom", align="center", font=("Comics MS", 15, "normal"))


# class Done(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.goto(0, 0)
#         self.color("White")
#         self.write("GAME OVER", align="center", font=("Times", 24, "normal"))

