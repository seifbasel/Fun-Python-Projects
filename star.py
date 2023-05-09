from turtle import *
tu=Turtle()
tu.speed(0)

def star():
    for i in range(5):
        tu.fd(100)
        tu.lt(215)
        tu.forward(50)

for i in range(100):
    tu.left(30)
    star()
    tu.fd(150)
    tu.right(100)



