import turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0



class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.head.color('green')

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = turtle.Turtle("square")
        snake_part.penup()
        snake_part.color('white')
        snake_part.goto(position)
        self.snake_segments.append(snake_part)

    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for snake_part in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[snake_part - 1].xcor()
            new_y = self.snake_segments[snake_part - 1].ycor()

            self.snake_segments[snake_part].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN_DIRECTION:
            self.head.setheading(UP_DIRECTION)

    def down(self):
        if self.head.heading() != UP_DIRECTION:
            self.head.setheading(DOWN_DIRECTION)

    def right(self):
        if self.head.heading() != LEFT_DIRECTION:
            self.head.setheading(RIGHT_DIRECTION)

    def left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.setheading(LEFT_DIRECTION)

    def reset_snake(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
        self.head.color('green')
