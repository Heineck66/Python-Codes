from turtle import Screen
from time import sleep

SNAKE_SPEED = 0.1


class Game:
    def __init__(self, title="snake") -> None:
        self.screen = Screen()
        self.screen.listen()
        self.screen.title(title)
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.is_on = True

    def update(self):
        sleep(SNAKE_SPEED)
        return self.screen.update()

    def exit(self):
        return self.screen.exitonclick()

    def add_listner(self, func, key):
        return self.screen.onkey(func, key)
