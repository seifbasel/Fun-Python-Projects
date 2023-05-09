from graphics import *


# flower with grapics library

#main window
window = GraphWin("Window",500,500)
window.setBackground("lightgray")

#text on top of text box
flagtext=Text(Point(250,220),"enter the requested number of petals in range from 1 to 6")
flagtext.draw(window)
flagtext.setFace("arial")
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



y=window.getMouse()
print(y)
x=(ent.getText())




if  int(x)==1:
    #flower
    flower_body=Oval(Point(230,370),Point(270,500))
    flower_body.draw(window)
    flower_body.setFill("green")

    flower_body1=Oval(Point(230,370),Point(260,500))
    flower_body1.draw(window)
    flower_body1.setFill("lightgray")
    flower_body1.setOutline("lightgray")

    floewr_head2=Circle(Point(251,376),23)
    floewr_head2.draw(window)
    floewr_head2.setFill("orange")
    floewr_head2.setOutline("yellow")

    floewr_head=Circle(Point(250,375),20)
    floewr_head.draw(window)
    floewr_head.setFill("yellow")
    floewr_head.setOutline("yellow")

    flower_paper1=Oval(Point(270,365),Point(330,380))
    flower_paper1.draw(window)
    flower_paper1.setFill("red")
    flower_paper1.setOutline("red")

    window.getMouse()

elif int(x)==2:
    #flower
    flower_body=Oval(Point(230,370),Point(270,500))
    flower_body.draw(window)
    flower_body.setFill("green")

    flower_body1=Oval(Point(230,370),Point(260,500))
    flower_body1.draw(window)
    flower_body1.setFill("lightgray")
    flower_body1.setOutline("lightgray")

    floewr_head2=Circle(Point(251,376),23)
    floewr_head2.draw(window)
    floewr_head2.setFill("orange")
    floewr_head2.setOutline("yellow")

    floewr_head=Circle(Point(250,375),20)
    floewr_head.draw(window)
    floewr_head.setFill("yellow")
    floewr_head.setOutline("yellow")

    flower_paper1=Oval(Point(270,365),Point(330,380))
    flower_paper1.draw(window)
    flower_paper1.setFill("red")
    flower_paper1.setOutline("red")


    flower_paper3=Oval(Point(170,365),Point(230,380))
    flower_paper3.draw(window)
    flower_paper3.setFill("red")
    flower_paper3.setOutline("red")

    window.getMouse()

elif int(x)==3:
#flower

    flower_body=Oval(Point(230,370),Point(270,500))
    flower_body.draw(window)
    flower_body.setFill("green")

    flower_body1=Oval(Point(230,370),Point(260,500))
    flower_body1.draw(window)
    flower_body1.setFill("lightgray")
    flower_body1.setOutline("lightgray")

    floewr_head2=Circle(Point(251,376),23)
    floewr_head2.draw(window)
    floewr_head2.setFill("orange")
    floewr_head2.setOutline("yellow")

    floewr_head=Circle(Point(250,375),20)
    floewr_head.draw(window)
    floewr_head.setFill("yellow")
    floewr_head.setOutline("yellow")

    flower_paper1=Oval(Point(270,365),Point(330,380))
    flower_paper1.draw(window)
    flower_paper1.setFill("red")
    flower_paper1.setOutline("red")


    flower_paper2=Oval(Point(244,300),Point(258,355))
    flower_paper2.draw(window)
    flower_paper2.setFill("red")
    flower_paper2.setOutline("red")



    flower_paper3=Oval(Point(170,365),Point(230,380))
    flower_paper3.draw(window)
    flower_paper3.setFill("red")
    flower_paper3.setOutline("red")



    window.getMouse()
elif int(x)==4:
#flower
    flower_body=Oval(Point(230,370),Point(270,500))
    flower_body.draw(window)
    flower_body.setFill("green")

    flower_body1=Oval(Point(230,370),Point(260,500))
    flower_body1.draw(window)
    flower_body1.setFill("lightgray")
    flower_body1.setOutline("lightgray")


    floewr_head2=Circle(Point(251,376),23)
    floewr_head2.draw(window)
    floewr_head2.setFill("orange")
    floewr_head2.setOutline("yellow")

    floewr_head=Circle(Point(250,375),20)
    floewr_head.draw(window)
    floewr_head.setFill("yellow")
    floewr_head.setOutline("yellow")



    flower_paper1=Oval(Point(270,365),Point(330,380))
    flower_paper1.draw(window)
    flower_paper1.setFill("red")
    flower_paper1.setOutline("red")

    flower_paper2=Oval(Point(244,300),Point(258,355))
    flower_paper2.draw(window)
    flower_paper2.setFill("red")
    flower_paper2.setOutline("red")

    flower_paper3=Oval(Point(170,365),Point(230,380))
    flower_paper3.draw(window)
    flower_paper3.setFill("red")
    flower_paper3.setOutline("red")

    flower_paper4=Oval(Point(244,395),Point(258,445))
    flower_paper4.draw(window)
    flower_paper4.setFill("red")
    flower_paper4.setOutline("red")
    window.getMouse()

elif int(x)==5:
#flower
    flower_body=Oval(Point(230,370),Point(270,500))
    flower_body.draw(window)
    flower_body.setFill("green")

    flower_body1=Oval(Point(230,370),Point(260,500))
    flower_body1.draw(window)
    flower_body1.setFill("lightgray")
    flower_body1.setOutline("lightgray")

    floewr_head2=Circle(Point(251,376),23)
    floewr_head2.draw(window)
    floewr_head2.setFill("orange")
    floewr_head2.setOutline("yellow")

    floewr_head=Circle(Point(250,375),20)
    floewr_head.draw(window)
    floewr_head.setFill("yellow")
    floewr_head.setOutline("yellow")

    flower_paper1=Oval(Point(270,365),Point(330,380))
    flower_paper1.draw(window)
    flower_paper1.setFill("red")
    flower_paper1.setOutline("red")


    flower_paper2=Oval(Point(244,300),Point(258,355))
    flower_paper2.draw(window)
    flower_paper2.setFill("red")
    flower_paper2.setOutline("red")


    flower_paper3=Oval(Point(170,365),Point(230,380))
    flower_paper3.draw(window)
    flower_paper3.setFill("red")
    flower_paper3.setOutline("red")


    flower_paper4=Oval(Point(244,395),Point(258,445))
    flower_paper4.draw(window)
    flower_paper4.setFill("red")
    flower_paper4.setOutline("red")

    flower_paper6=Polygon(Point(235,360),Point(195,335),Point(215,337),Point(215,315))
    flower_paper6.draw(window)
    flower_paper6.setFill("red")
    flower_paper6.setOutline("red")

    window.getMouse()

elif int(x)==6:
#flower
    flower_body=Oval(Point(230,370),Point(270,500))
    flower_body.draw(window)
    flower_body.setFill("green")

    flower_body1=Oval(Point(230,370),Point(260,500))
    flower_body1.draw(window)
    flower_body1.setFill("lightgray")
    flower_body1.setOutline("lightgray")

    floewr_head2=Circle(Point(251,376),23)
    floewr_head2.draw(window)
    floewr_head2.setFill("orange")
    floewr_head2.setOutline("yellow")

    floewr_head=Circle(Point(250,375),20)
    floewr_head.draw(window)
    floewr_head.setFill("yellow")
    floewr_head.setOutline("yellow")
    
    flower_paper1=Oval(Point(270,365),Point(330,380))
    flower_paper1.draw(window)
    flower_paper1.setFill("red")
    flower_paper1.setOutline("red")


    flower_paper2=Oval(Point(244,300),Point(258,355))
    flower_paper2.draw(window)
    flower_paper2.setFill("red")
    flower_paper2.setOutline("red")


    flower_paper3=Oval(Point(170,365),Point(230,380))
    flower_paper3.draw(window)
    flower_paper3.setFill("red")
    flower_paper3.setOutline("red")


    flower_paper4=Oval(Point(244,395),Point(258,445))
    flower_paper4.draw(window)
    flower_paper4.setFill("red")
    flower_paper4.setOutline("red")


    flower_paper5=Polygon(Point(266,361),Point(290,315),Point(291,340),Point(308,340))
    flower_paper5.draw(window)
    flower_paper5.setFill("red")
    flower_paper5.setOutline("red")


    flower_paper6=Polygon(Point(235,360),Point(195,335),Point(215,337),Point(215,315))
    flower_paper6.draw(window)
    flower_paper6.setFill("red")
    flower_paper6.setOutline("red")

    window.getMouse()


else:
    #error
    print("wrong entry")
    wrong_text=Text(Point(250,370),"wrong entery")
    wrong_text.setSize(30)
    wrong_text.setFill("black")
    wrong_text.setFace("arial")
    wrong_text.draw(window)
    window.getMouse()