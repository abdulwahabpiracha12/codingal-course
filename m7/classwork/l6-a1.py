import turtle

sc = turtle.Screen()

sc.bgcolor("sky blue")

sc.setup(500, 500)

turtle.title("Welcome to Turtle Window")


board = turtle.Turtle()

n = 6

for i in range(n):
    board.forward(100)
    board.left(360/n)

turtle.done()