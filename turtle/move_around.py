import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Move the Block")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Create the block
block = turtle.Turtle()
block.shape("square")
block.color("blue")
block.penup()

# Define the block's movement functions
def move_up():
    y = block.ycor()
    block.sety(y + 20)

def move_down():
    y = block.ycor()
    block.sety(y - 20)

def move_left():
    x = block.xcor()
    block.setx(x - 20)

def move_right():
    x = block.xcor()
    block.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Main game loop
while True:
    wn.update()
