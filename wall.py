from turtle import Turtle
INITIAL_TOP_X = -310
INITIAL_TOP_Y = 310
INITIAL_RIGHT_X = 310
INITIAL_RIGHT_Y = 310
INITIAL_BOTTOM_X = 310
INITIAL_BOTTOM_Y = -310
INITIAL_LEFT_X = -310
INITIAL_LEFT_Y = -310


class Wall:
    def __init__(self):

        self.wall_segments = []
        self.create_wall()

    def create_top(self):
        for i in range(0, 620, 20):
            wall_segment = Turtle("square")
            wall_segment.shapesize(stretch_wid=2, stretch_len=2)
            wall_segment.penup()
            wall_segment.color("red")
            wall_segment.goto(INITIAL_TOP_X+i, INITIAL_TOP_Y)
            self.wall_segments.append(wall_segment)

    def create_right(self):
        for i in range(0, 620, 20):
            wall_segment = Turtle("square")
            wall_segment.shapesize(stretch_wid=2, stretch_len=2)
            wall_segment.penup()
            wall_segment.color("red")
            wall_segment.goto(INITIAL_RIGHT_X, INITIAL_RIGHT_Y-i)
            self.wall_segments.append(wall_segment)

    def create_bottom(self):
        for i in range(0, 620, 20):
            wall_segment = Turtle("square")
            wall_segment.shapesize(stretch_wid=2, stretch_len=2)
            wall_segment.penup()
            wall_segment.color("red")
            wall_segment.goto(INITIAL_BOTTOM_X-i, INITIAL_BOTTOM_Y)
            self.wall_segments.append(wall_segment)

    def create_left(self):
        for i in range(0, 620, 20):
            wall_segment = Turtle("square")
            wall_segment.shapesize(stretch_wid=2, stretch_len=2)
            wall_segment.penup()
            wall_segment.color("red")
            wall_segment.goto(INITIAL_LEFT_X, INITIAL_LEFT_Y+i)
            self.wall_segments.append(wall_segment)

    def create_wall(self):

        self.create_top()
        self.create_right()
        self.create_bottom()
        self.create_left()
