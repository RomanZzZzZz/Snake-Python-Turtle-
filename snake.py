from turtle import *
import random


def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    

class Head(Turtle):
  def __init__(self, screen, body):
    super().__init__()
    self.shape("square")
    self.color(generate_color())
    self.penup()
    self.goto(0, 0)
    self.direction = "up"
    self.alive = True


  def up(self):
    if self.direction != "down":
      self.setheading(90)
      self.direction = "up"


  def down(self):
    if self.direction != "up":
      self.setheading(270)
      self.direction = "down"


  def left(self):
    if self.direction != "right":
      self.setheading(180)
      self.direction = "left"


  def right(self):
    if self.direction != "left":
      self.setheading(0)
      self.direction = "right"


  def move(self):
    self.forward(20)
    if self.xcor() > 240 or self.xcor() < -240 or self.ycor() > 240 or self.ycor() < -240:
      self.die()

  def die(self):
    self.hideturtle()
    self.alive = False
    for s in body[1:]:
      s.hideturtle()


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.shape("square")
    self.color(other.pencolor())
    self.penup()
    self.goto(other.xcor(), other.ycor())


  def move(self, other):
    self.goto(other.xcor(), other.ycor())


class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color(generate_color())
    self.penup()
    self.goto(random.randint(-230, 230), random.randint(-230, 230))


  def relocate(self):
    self.goto(random.randint(-230, 230), random.randint(-230, 230))


screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)


playing_area()


body = []
head = Head(screen, body)
body.append(head)
body.append(Segment(head))
apple = Apple()


# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()
screen.onkey(head.up, "w")
screen.onkey(head.down, "s")
screen.onkey(head.left, "a")
screen.onkey(head.right, "d")


def game_loop():
  if head.alive:
    for i in range(len(body) - 1, 0, -1):
      body[i].move(body[i - 1])
    head.move()

    if head.distance(apple) < 20:
      apple.relocate()
      body.append(Segment(body[-1]))

    for segment in body[3:]:
      if head.distance(segment) < 20:
        head.die()

  screen.ontimer(game_loop, 150)


screen.onkey(game_loop, "space")


screen.exitonclick()