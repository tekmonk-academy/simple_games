"""
Pong Game Part 1

The ball moves free
Paddles are moveable

Author: Tu Bui
"""

import time
import turtle

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(5, 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(5, 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

def paddle_a_up():
  if paddle_a.ycor() > 200:
    return
  paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
  if paddle_a.ycor() < -200:
    return
  paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
  if paddle_b.ycor() > 200:
    return
  paddle_b.sety(paddle_b.ycor())

def paddle_b_down():
  if paddle_b.ycor() < -200:
    return
  paddle_b.sety(paddle_b.ycor())

# Keyboard handler
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

score_a, score_b = 0, 0
dx = 2
dy = 2

while True:
  screen.update()

  ball.goto(ball.xcor() + dx, ball.ycor() + dy)

  time.sleep(0.01)