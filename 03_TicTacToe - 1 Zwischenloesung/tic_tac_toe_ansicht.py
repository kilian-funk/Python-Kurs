from turtle import *
from tic_tac_toe_modell import Pos, Zustand, Belegung

class Ansicht():
    def __init__(self):
        self.linien = [
            (0,-300,-100),
            (0,-300,100),
            (90,-100,-300),
            (90,100,-300)
        ]
        register_shape("kreuz", (
            (50, 50), (-50, -50), (0, 0), (50, -50), (-50,50), (0,0)
        ))

        register_shape("kreis", (
            (50,0), (45,20), (40,30), (30,40), (20,45),
            (0,50), (-20,45), (-30,40), (-40,30), (-45,20),
            (-50,0), (-45,-20), (-40,-30), (-30,-40), (-20,-45),
            (0,-50), (20,-45), (30,-40), (40,-30), (45,-20),
        ))
        
        self.feld_positionen = {
            Pos.OBEN_LINKS: (-200,200),
            Pos.OBEN_MITTE: (0, 200),
            Pos.OBEN_RECHTS: (200, 200),
            Pos.MITTE_LINKS: (-200,0),
            Pos.MITTE_MITTE: (0, 0),
            Pos.MITTE_RECHTS: (200,0),
            Pos.UNTEN_LINKS: (-200, -200),
            Pos.UNTEN_MITTE: (0, -200),
            Pos.UNTEN_RECHTS: (200, -200),
        }

        self.loesche_spielfeld()
        self.stift = Turtle()
        self.stift.speed(0)
        self.stift.penup()

    def zeichne_spielfeld(self):
        print("Neues leeres Spielfeld")
        
        for linie in self.linien:
            self.stift.setheading(linie[0])           
            self.stift.goto(linie[1],linie[2])
            self.stift.pendown()
            self.stift.forward(600)
            self.stift.penup()

    def loesche_spielfeld(self):
        print("Spielfeld wird geloescht")
        clearscreen()
    
    def zeichne_symbol(self, position, art):
        print(f"{art} an {position} gesetzt")
        self.stift.shape("kreuz" if art == Belegung.KREUZ else "kreis")
        self.stift.goto(*self.feld_positionen[position])
        self.stift.stamp()   
        
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
    
    
        
    
