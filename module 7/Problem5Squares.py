# Sezimgul
# 2026-11-03
# Problem 5: Draw nested squares with the turtle, using drawSquare


import turtle


def drawSquare(t, sz):
    # Get turtle t to draw a square of sz side
    for i in range(4):
        t.forward(sz)
        t.left(90)


def main():
    wn = turtle.Screen()    # Set up the window
    alex = turtle.Turtle()  # Create the turtle
    alex.color("blue")

    size = 20               # Side of the smallest square
    for _ in range(5):      # Draw 5 nested squares
        drawSquare(alex, size)
        size = size + 20    # Each new square is bigger
        # Move to the starting corner of the next, bigger square
        alex.penup()
        alex.backward(10)
        alex.right(90)
        alex.forward(10)
        alex.left(90)
        alex.pendown()

    wn.exitonclick()        # Close the window on click


main()
