import random
from turtle import *

def petal_draw(turtle, colors, petal_number):
    for _ in range(int(petal_number)):
        turtle.width(10)
        turtle.color(random.choice(colors))
        turtle.circle(200, 90, 100)
        turtle.left(90)
        turtle.color(random.choice(colors))
        turtle.circle(200, 90, 100)
        turtle.left(20)

def main():
    bgcolor("black")
    tu = Turtle()
    tu.speed(0)

    # Give random color
    colors = ["red", "blue", "gray", "purple", "light blue", "green", "pink", "antiquewhite1", "brown1",
              "darkorchid", "deeppink2", "gold1", "indianred1", "magenta", "light green", "skyblue4"]
    
    chosen_color = random.choice(colors)

    # Petal numbers entry
    petal_number = numinput("Number of Petals", "Enter the number of petals (5 to 100)", 5, 1, 100)

    # Draw petals
    petal_draw(tu, colors, petal_number)

    done()

if __name__ == "__main__":
    main()
