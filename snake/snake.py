from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POS:
            self.add_seg(position)
        self.head = self.segments[0]

    def extend(self):
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        self.add_seg((x, y))

    def add_seg(self, position):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def change_color(self, color):
        for seg in self.segments:
            seg.color(color)

    def move(self):
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_idx - 1].xcor()
            y = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
