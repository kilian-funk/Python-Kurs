from turtle import *
import math
import time

def neuer_stift(farbe):
    stift = Turtle()
    stift.speed(0)
    stift.pencolor(farbe)
    stift.pensize(3)
    stift.shape("circle")
    stift.shapesize(.3,.3,1)
    stift.penup()
    stift.goto(0,-radius)
    stift.pendown()
    return stift
   

def zeichne_innen_polygon(seiten, radius = 200):
    stift = neuer_stift("red")
    halber_winkel = 180/seiten
    seitenlaenge_innen = 2*radius*math.sin(halber_winkel*math.pi/180)
    
    for seite in range(seiten):
        stift.left(halber_winkel)
        stift.forward(seitenlaenge_innen)
        stift.left(halber_winkel)

def zeichne_aussen_polygon(seiten, radius):
    stift = neuer_stift("blue")
    
    halber_winkel = 180/seiten
    seitenlaenge_aussen = 2*radius*math.tan(halber_winkel*math.pi/180)
    for seite in range(seiten):
        stift.forward(seitenlaenge_aussen/2)
        stift.left(2*halber_winkel)
        stift.forward(seitenlaenge_aussen/2)


for seiten in [6, 12, 24, 48]:
    radius = 200
    
    halber_winkel = 180/seiten
    seitenlaenge_innen = 2*math.sin(halber_winkel*math.pi/180)
    seitenlaenge_aussen = 2*math.tan(halber_winkel*math.pi/180)
    print("Näherung von PI aus {:3d}-seitigem Polygon: [{:07.4f}; {:07.4f}]".format(seiten,
                                                                               seitenlaenge_innen*seiten/2,
                                                                               seitenlaenge_aussen*seiten/2))
    zeichne_innen_polygon(seiten, radius)
    zeichne_aussen_polygon(seiten, radius)
    time.sleep(2)
    