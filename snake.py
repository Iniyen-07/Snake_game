from turtle import Screen,Turtle
Starting_point=[(0,0),(-20,0),(-40,0)]
distance=20
up=90
down=270
left=180
right=0

class Snake:
    def __init__(self):
        self.objects=[]
        self.create_snake()
        self.head=self.objects[0]
    def create_snake(self):
        for pos in Starting_point:
            self.add_objects(pos)

    def add_objects(self,pos):
        a = Turtle("square")
        a.color("white")
        a.penup()
        a.goto(pos)
        self.objects.append(a)

    def extend(self):
        self.add_objects(self.objects[-1].position())

    def move_snake(self):
        for i in range(len(self.objects) - 1, 0, -1):
            new_x = self.objects[i - 1].xcor()
            new_y = self.objects[i - 1].ycor()
            self.objects[i].goto(new_x, new_y)
        self.head.forward(distance)

    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)