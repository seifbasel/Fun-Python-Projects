from time import sleep
from graphics import *


win =GraphWin("window",500,500)
win.setBackground("white")


#face
face2=Circle(Point(255,255),100)  
face2.draw(win)                       
face2.setOutline("orange")         
face2.setFill("orange")

face=Circle(Point(250,250),100)  
face.draw(win)                       
face.setOutline("yellow")         
face.setFill("yellow")


#mouse
mouse=Circle(Point(250,285),35) 
mouse.draw(win)
mouse.setFill("black")

# #tounge
# tounge=Oval(Point(220,300),Point(280,320)) 
# tounge.draw(win)
# tounge.setFill("red")

#mouse2
mouse2=Oval(Point(200,245),Point(300,290)) 
mouse2.draw(win)
mouse2.setFill("yellow")
mouse2.setOutline("yellow")


#left eye
lefteye=Circle(Point(220,235),15) 
lefteye.draw(win)
lefteye.setFill("white")



#right eye
righteye=Circle(Point(280,235),15) 
righteye.draw(win)
righteye.setFill("white")

# glasses

glassleft=Polygon(Point(200,225),Point(240,225),Point(240,245),Point(220,255),Point(200,245)) 
glassleft.draw(win)
glassleft.setFill("white")
glassleft.setWidth(7)
glassleft.setOutline("black")

glassright=Polygon(Point(260,225),Point(300,225),Point(300,245),Point(280,255),Point(260,245)) 
glassright.draw(win)
glassright.setFill("white")
glassright.setWidth(7)
glassright.setOutline("black")


glassright2=Line(Point(300,235),Point(340,220))
glassright2.draw(win)
glassright2.setWidth(10)

glassleft2=Line(Point(200,235),Point(160,220))
glassleft2.draw(win)
glassleft2.setWidth(10)

glasscenter=Line(Point(240,235),Point(260,235))
glasscenter.draw(win)
glasscenter.setWidth(10)

#teeth
teethcenter=Line(Point(245,300),Point(245,290))
teethcenter.draw(win)
teethcenter.setWidth(10)
teethcenter.setFill("white")

teethcenter2=Line(Point(260,300),Point(260,290))
teethcenter2.draw(win)
teethcenter2.setWidth(10)
teethcenter2.setFill("white")


#left eyelash
lefteyelash=Polygon(Point(244,205),Point(200,190),Point(200,200)) 
lefteyelash.draw(win)
lefteyelash.setFill("black")

#right eyelash
righteyelash=Polygon(Point(260,205),Point(300,190),Point(300,200))
righteyelash.draw(win)
righteyelash.setFill("black")

#left eye inner
leftinner=Circle(Point(220,235),7) 
leftinner.draw(win)
leftinner.setFill("black")

#right eye inner
rightinner=Circle(Point(280,235),7) 
rightinner.draw(win)
rightinner.setFill("black")



for i in range (20):
    glasscenter.move(-7.5,0)
    glassleft.move(-7.5,0)
    glassleft2.move(-7.5,0)
    glassright.move(-7.5,0)
    glassright2.move(-7.5,0)
    teethcenter.move(-7.5,0)
    teethcenter2.move(-7.5,0)
    lefteye.move(-7.5,0)
    righteye.move(-7.5,0)
    leftinner.move(-7.5,0)
    rightinner.move(-7.5,0)
    mouse.move(-7.5,0)
    mouse2.move(-7.5,0)
    face.move(-7.5,0)
    face2.move(-7.5,0)
    righteyelash.move(-7.5,-.5)
    lefteyelash.move(-7.5,-.5)
    time.sleep(.02)

for i in range (40):
    glasscenter.move(7.5,0)
    glassleft.move(7.5,0)
    glassleft2.move(7.5,0)
    glassright2.move(7.5,0)
    glassright.move(7.5,0)
    teethcenter.move(7.5,0)
    teethcenter2.move(7.5,0)
    lefteye.move(7.5,0)
    leftinner.move(7.5,0)
    righteye.move(7.5,0)
    rightinner.move(7.5,0)
    mouse.move(7.5,0)
    mouse2.move(7.5,0)
    face.move(7.5,0)
    face2.move(7.5,0)
    righteyelash.move(7.5,.6)
    lefteyelash.move(7.5,.6)
    time.sleep(.02)


for i in range (20):
    glasscenter.move(-7.5,0)
    glassleft.move(-7.5,0)
    glassright.move(-7.5,0)
    glassleft2.move(-7.5,0)
    glassright2.move(-7.5,0)
    teethcenter.move(-7.5,0)
    teethcenter2.move(-7.5,0)
    lefteye.move(-7.5,0)
    leftinner.move(-7.5,0)
    rightinner.move(-7.5,0)
    righteye.move(-7.5,0)
    mouse.move(-7.5,0)
    mouse2.move(-7.5,0)
    face.move(-7.5,0)
    face2.move(-7.5,0)
    righteyelash.move(-7.5,-.5)
    lefteyelash.move(-7.5,-.5)
    time.sleep(.02)

win.getMouse()
win.close()
