from turtle import *
from tic_tac_toe_modell import Pos, Zustand

class Ansicht():
    
    def zeichne_spielfeld(self):
        print("Neues leeres Spielfeld")
        stift = Turtle()
        stift.speed(0)

        stift.penup()
        stift.goto(-300,-100)
        stift.pendown()
        stift.forward(600)
        stift.penup()       
        stift.goto(-300,100)
        stift.pendown()
        stift.forward(600)
        stift.penup()      
        stift.left(90)           
        stift.goto(-100,-300)
        stift.pendown()
        stift.forward(600)
        stift.penup()       
        stift.goto(100,-300)
        stift.pendown()
        stift.forward(600)


    def loesche_spielfeld(self):
        print("Spielfeld wird geloescht")
    
    def zeichne_symbol(self, position, art):
        print(f"{art} an {position} gesetzt")

        register_shape("kreuz", (
            (50, 50), (-50, -50), (0, 0), (50, -50), (-50,50), (0,0)
        ))

        register_shape("kreis", (
            (50,0), (45,20), (40,30), (30,40), (20,45),
            (0,50), (-20,45), (-30,40), (-40,30), (-45,20),
            (-50,0), (-45,-20), (-40,-30), (-30,-40), (-20,-45),
            (0,-50), (20,-45), (30,-40), (40,-30), (45,-20),
        ))

        stift = Turtle()
        stift.penup()
        stift.shape("kreuz")
        stift.goto(-200,200)
        stift.stamp()
       
        
        
        
    def berichte_zustand(self, zustand):
        print(zustand.value)
        
        
    def position_aus_eingabe(self, geraete_pos):
        
        pos_abbildung={
            "oben links": Pos.OBEN_LINKS,
            "oben mitte": Pos.OBEN_MITTE,
            "oben rechts": Pos.OBEN_RECHTS,
            "mitte links": Pos.MITTE_LINKS,
            "mitte mitte": Pos.MITTE_MITTE,
            "mitte rechts": Pos.MITTE_RECHTS,
            "unten links": Pos.UNTEN_LINKS,
            "unten mitte": Pos.UNTEN_MITTE,
            "unten rechts": Pos.UNTEN_RECHTS,
        }
        
        return pos_abbildung.get(geraete_pos, None)
    
    
        
    
