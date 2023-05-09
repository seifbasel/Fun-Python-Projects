import random
from turtle import *
tu=Turtle()
bgcolor("black")
tu.speed(0)

# give random color
color=["red","blue","gray","purple","light blue","green","pink","antiquewhite1","brown1",
"darkorchid","deeppink2","gold1","indianred1","magenta","light green","skyblue4"]
chosen_color=random.choice(color)

# petal numbers entery
petal_number=numinput("number of petals","enter the number of petals that you want from ( 5 to 100 )",5,1,100)

# draw petals 
def petal_draw(petal_number):
    for i in range(int(petal_number)):
        tu.width(10)
        tu.color(random.choice(color))
        tu.circle(200,90,100)
        tu.left(90)
        tu.color(random.choice(color))
        tu.circle(200,90,100)
        tu.left(20)
        
petal_draw(petal_number)
done()