from turtle import *
import time


stift = Turtle()
time.sleep(2)

for _ in range(4):
    stift.forward(200)
    stift.left(90)
    stift.dot(20)

time.sleep(2)

stift.up()
stift.goto(0,-100)
stift.color("red")
stift.width(5)
stift.down()

for _ in range(9):
    stift.forward(100)
    stift.right(160)
    
time.sleep(2)

stift.up()
stift.goto(-200,0)
stift.color("blue", "green")
stift.down()

stift.begin_fill()
stift.circle(100,180)
stift.end_fill()
        
time.sleep(2)

stift.up()
register_shape("ufo", ((0,0), (-10,-10), (-1,0), (-3,0), (-5,2), (-6,5), (-5,8), \
                       (-3,10), (3,10), (5,8), (6,5), (5,2), (3,0), (1,0), (10,-10), (0,0)))
stift.shape("ufo")
stift.shapesize(3,3)
stift.goto(-100,-100)
stift.setheading(90)
stift.speed(0)

def wenn_maus_gezogen(x,y):
    stift.goto(x,y)
    
stift.ondrag(wenn_maus_gezogen)
mainloop()


