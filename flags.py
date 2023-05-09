from graphics import *

#main window
window = GraphWin("Window",500,500)
window.setBackground("lightgray")

#text on top of text box
flagtext=Text(Point(250,220),"enter country name from ( iraq ) or ( syria )")
flagtext.draw(window)
flagtext.setFace("helvetica")
flagtext.setStyle("bold")

#text box
ent=Entry(Point(250,250),20)
ent.setFill("white")
ent.draw(window)

#button bg
button_bg=Rectangle(Point(220,270),Point(280,290))
button_bg.draw(window)
#button
button=Text(Point(250,280),"submit")
button.setFace("helvetica")
button.setStyle("bold")
button.setOutline("black")
button.draw(window)


window.getMouse()
x=ent.getText()


if x=="iraq":
    #iraq flag
    iraq_flag1=Rectangle(Point(100,300),Point(400,350))
    iraq_flag1.setFill("red")
    iraq_flag2=Rectangle(Point(100,350),Point(400,400))
    iraq_flag2.setFill("white")
    iraq_text=Text(Point(250,375),"الله اكبر")
    iraq_text.setSize(30)
    iraq_text.setFill("green")
    iraq_text.setFace("helvetica")
    iraq_flag3=Rectangle(Point(100,400),Point(400,450))
    iraq_flag3.setFill("black")
    iraq_flag1.draw(window)
    iraq_flag2.draw(window)
    iraq_flag3.draw(window)
    iraq_text.draw(window)
elif x=="syria":
    #syria flag
    syria_flag1=Rectangle(Point(100,300),Point(400,350))
    syria_flag1.setFill("red")
    syria_flag2=Rectangle(Point(100,350),Point(400,400))
    syria_flag2.setFill("white")
    star1=Polygon(Point(250,370),Point(260,370),Point(270  ,360),Point(280,370),Point(290,370),Point(280,380),Point(285,390),Point(270,385),Point(255,390),Point(260,380))
    star1.setFill("green")
    star1.setWidth(0)
    star2=Polygon(Point(200,370),Point(210,370),Point(220  ,360),Point(230,370),Point(240,370),Point(230,380),Point(235,390),Point(220,385),Point(205,390),Point(210,380))
    star2.setFill("green")
    star2.setWidth(0)
    syria_flag3=Rectangle(Point(100,400),Point(400,450))
    syria_flag3.setFill("black")
    syria_flag1.draw(window)
    syria_flag2.draw(window)
    star1.draw(window)
    syria_flag3.draw(window)
    star2.draw(window)
else:
    print("wrong entry")
    wrong_text=Text(Point(250,370),"wrong entery")
    wrong_text.setSize(30)
    wrong_text.setFill("black")
    wrong_text.setFace("arial")
    wrong_text.draw(window)

print(x)
window.getMouse()
