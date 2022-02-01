from turtle import Turtle
from random import randint, randrange

COLOR_LIST = ["red", "blue", "Green", "yellow"]


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.__actual_color = "blue"
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("blue")
        self.refresh()

    def get_current_color(self):
        return self.__actual_color

    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.__actual_color = COLOR_LIST[randrange(0, 4)]
        self.color(self.__actual_color)
        self.goto(rand_x, rand_y)
