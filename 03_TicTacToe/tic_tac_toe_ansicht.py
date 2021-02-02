from turtle import *
from tic_tac_toe_modell import Pos, Zustand, Belegung

class Ansicht():
    
    def zeichne_spielfeld(self):
        print("Neues leeres Spielfeld...")
        
    def loesche_spielfeld(self):
        print("Spielfeld wird geloescht")
    
    def zeichne_symbol(self, position, art):
        print(f"{art} an {position} gesetzt")
        
    def berichte_zustand(self, zustand):
        zustands_meldung = {
            Zustand.OK: "Alles in Ordnung",
            Zustand.NICHT_ERLAUBT: "Zug ist nicht erlaubt",
            Zustand.KREUZ_GEWINNT: "Das Spiel ist beendet. Kreuz gewinnt!",
            Zustand.KREIS_GEWINNT: "Das Spiel ist beendet. Kreis gewinnt!",
            Zustand.UNENTSCHIEDEN: "Das Spiel endet unentschieden.",
            Zustand.KREIS_IST_AM_ZUG: "Kreis ist am Zug.",
            Zustand.KREUZ_IST_AM_ZUG: "Kreuz ist am Zug.",
        }
        print(zustands_meldung[zustand])
        
        
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
    
    
        
    
