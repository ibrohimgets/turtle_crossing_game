from turtle import Turtle

# Details
start_position = (0, -270)
move_distance = 10
finish_lineY = 230

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
    
    def go_up(self):
        self.forward(move_distance)

    def go_down(self):
        self.backward(move_distance)
    
    def go_to_start(self):
        self.goto(start_position)
    
    def finish_line(self):
        return self.ycor() > finish_lineY
