from turtle import *
from tic_tac_toe_modell import Pos, Zustand, Belegung
import time

class Ansicht():
    
    def zeichne_spielfeld(self):
        print("Neues leeres Spielfeld...")
        stift = Turtle()
        time.sleep(2)

        stift.forward(200)
        stift.left(90)
        stift.dot(20)

        
    def loesche_spielfeld(self):
        print("Spielfeld wird geloescht")
    
    def zeichne_symbol(self, position, art):
        print(f"{art} an {position} gesetzt")
        
    def berichte_zustand(self, zustand):
        print(zustand.value)
        
        
    def position_aus_eingabe(geraete_pos):
        
        pos_abbildung={
            "oben links": Pos.OBEN_LINKS,
            "oben mitte": Pos.OBEN_MITTE,
            "oben rects": OBEN_RECHTS,
            "mitte links": MITTE_LINKS,
            "mitte mitte": MITTE_MITTE,
            "mitte rechts": MITTE_RECHTS,
            "unten links": UNTEN_LINKS,
            "unten mitte": UNTEN_MITTE,
            "unten rechts": UNTEN_RECHTS,
        }
        
        return pos_abbildung.get(geraete_pos, None)
    
    
        
    
