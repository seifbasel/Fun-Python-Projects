from turtle import *

tu=Turtle()
bgcolor("lightblue")
tu.speed(0)

# ground
tu.penup()
tu.goto(-500,0)
tu.pendown()
tu.width(250)
tu.color("green")
tu.forward(1000)

# sea ground
tu.penup()
tu.goto(-500,-250)
tu.pendown()
tu.width(300)
tu.color("#1a75ff", "#1a75ff")
tu.forward(1000)


# sun
tu.penup()
tu.goto(-360,320)
tu.pendown()
tu.color("yellow")
tu.width(150)
tu.dot()
tu.penup()
tu.home()

# sky
def sky(x,y):
	tu.goto(x,y)
	tu.color("white","white")
	tu.begin_fill()
	tu.circle(50)
	tu.forward(50)
	tu.circle(50)
	tu.right(90)
	tu.circle(50)
	tu.right(90)
	tu.circle(50)
	tu.right(90)
	tu.circle(50)
	tu.right(90)
	tu.circle(50)
	tu.end_fill()
	tu.home()

sky(300,300)
sky(170,250)
sky(40,300)
sky(-90,250)

#go to sea start point
tu.penup()
tu.backward(500)
tu.right(90)
tu.forward(300)
# first wave
tu.pendown()
for i in range(9):
	tu.color('#005ce6','#005ce6')
	tu.width(30)
	tu.circle(50,180,50)
	tu.right(180)
	tu.circle(50,-180,50)
	tu.right(180)
#go to sea start point
tu.penup()
tu.home()
tu.backward(500)
tu.right(90)
tu.forward(250)
tu.pendown()
# second wave
for i in range(9):
	tu.color('#005ce6','#005ce6')
	tu.width(30)
	tu.circle(50,180,50)
	tu.right(180)
	tu.circle(50,-180,50)
	tu.right(180)


#go to sea start point
tu.penup()
tu.home()
tu.backward(500)
tu.right(90)
tu.forward(200)
tu.pendown()
# third wave
for i in range(9):
	tu.color('#005ce6','#005ce6')
	tu.width(30)
	tu.circle(50,180,50)
	tu.right(180)
	tu.circle(50,-180,50)
	tu.right(180)

#go to sea start point
tu.penup()
tu.home()
tu.backward(500)
tu.right(90)
tu.forward(350)
tu.pendown()
# forth wave
for i in range(9):
	tu.color('#005ce6','#005ce6')
	tu.width(30)
	tu.circle(50,180,50)
	tu.right(180)
	tu.circle(50,-180,50)
	tu.right(180)

tu.penup()
tu.home()


# # move rainbow to start point
tu.penup()
tu.right(90)
tu.forward(90)
tu.left(90)

# violet
tu.forward(200)
tu.left(90)
tu.pendown()
tu.color("violet","violet")
tu.width(20)
tu.circle(200,180,50)

# indigo
tu.right(270)
tu.forward(420)
tu.left(90)
tu.color("indigo","indigo")
tu.circle(220,180,50)

# blue
tu.right(270)
tu.forward(460)
tu.left(90)
tu.color("blue","blue")
tu.circle(240,180,50)

# green
tu.right(270)
tu.forward(500)
tu.left(90)
tu.color("green","green")
tu.circle(260,180,50)

# yellow
tu.right(270)
tu.forward(540)
tu.left(90)
tu.color("yellow","yellow")
tu.circle(280,180,50)

# orange
tu.right(270)
tu.forward(580)
tu.left(90)
tu.color("orange","orange")
tu.circle(300,180,50)

# red
tu.right(270)
tu.forward(620)
tu.left(90)
tu.color("red","red")
tu.circle(320,180,50)

# white
tu.color('green','green')
tu.right(270)
tu.forward(640)

done()
# mainloop()