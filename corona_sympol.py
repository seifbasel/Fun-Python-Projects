from turtle import *
tu=Turtle()
bgcolor("black")

x=100
y=100
z=100

tu.hideturtle()
# draw corona sympol 
for i in range(70):
    tu.speed(0)
    tu.color("red")
    tu.fillcolor()
    tu.width(2)
    tu.circle(50,100,10)
    tu.width(3)
    tu.end_fill()
    tu.color("green")
    tu.shape("circle")
    tu.forward(x)
    tu.left(y)
    tu.forward(z)
    x+=1
    y+=1
    z+=1

tu.hideturtle()
done()