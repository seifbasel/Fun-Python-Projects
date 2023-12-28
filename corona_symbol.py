from turtle import *

def draw_circle(turtle, radius, angle, color):
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius, angle)
    turtle.end_fill()

bgcolor("black")

tu = Turtle()
tu.hideturtle()

x = 100
y = 100
z = 100

# draw coronavirus symbol
for i in range(70):
    tu.speed(0)
    
    # Draw a red circle
    draw_circle(tu, 50, 100, "red")
    
    # Draw a green circle
    tu.color("green")
    tu.shape("circle")
    tu.forward(x)
    tu.left(y)
    tu.forward(z)
    
    x += 1
    y += 1
    z += 1

tu.hideturtle()
done()
