from enum import Enum

class Pos(Enum):
    OBEN_LINKS = "oben links"
    OBEN_MITTE = "oben mitte"
    OBEN_RECHTS = "oben rechts"
    MITTE_LINKS = "mitte links"
    MITTE_MITTE = "mitte mitte"
    MITTE_RECHTS = "mitte rechts"
    UNTEN_LINKS = "unten links"
    UNTEN_MITTE = "unten mitte"
    UNTEN_RECHTS = "unten rechts"
    

class Belegung(Enum):
    FREI = "Frei"
    KREIS = "Kreis"
    KREUZ = "Kreuz"


class Zustand(Enum):
    OK = "Alles in Ordnung."
    NICHT_ERLAUBT = "Der Zug ist nicht erlaubt."
    KREUZ_GEWINNT = "Das Spiel ist beendet. Kreuz gewinnt!"
    KREIS_GEWINNT = "Das Spiel ist beendet. Kreis gewinnt!"
    UNENTSCHIEDEN = "Das Spiel ist beendet. Unentschieden!"
    KREIS_IST_AM_ZUG = "Kreis ist am Zug."
    KREUZ_IST_AM_ZUG = "Kreuz ist am Zug."
    
    
class TicTacToe:
    
    def __init__(self, ausgabe):
        self._ausgabe = ausgabe
        self._ausgabe.zeichne_spielfeld()
        
        self._spielfeld = { feld: Belegung.FREI for feld in Pos}
        self._zustand = Zustand.KREUZ_IST_AM_ZUG
    
    def setze(self, pos, symbol):
        # Prüfe, of Spielzug erlaubt ist. Zug abbrechen, wenn nicht
        if not (
            self._spielfeld[pos] == Belegung.FREI and (
            (symbol == Belegung.KREUZ and self.zustand() == Zustand.KREUZ_IST_AM_ZUG) or
            (symbol == Belegung.KREIS and self.zustand() == Zustand.KREIS_IST_AM_ZUG)
        )):
            return Zustand.NICHT_ERLAUBT
        
        # Führe Spielzug aus
        print(pos,symbol)
        self._spielfeld[pos] = symbol
        self._zustand = Zustand.KREUZ_IST_AM_ZUG if symbol == Belegung.KREIS \
                            else Zustand.KREIS_IST_AM_ZUG

        self._ausgabe.zeichne_symbol(pos, symbol)
        
        if self.pruefe_auf_unentschieden():
            self._zustand = Zustand.UNENTSCHIEDEN
            return self._zustand
            
        if self.pruefe_auf_gewonnen(Belegung.KREUZ):
            self._zustand = Zustand.KREUZ_GEWINNT
            return self._zustand
            
        if self.pruefe_auf_gewonnen(Belegung.KREIS):
            self._zustand = Zustand.KREIS_GEWINNT   
            return self._zustand
        
        return Zustand.OK
    
    def pruefe_auf_unentschieden(self):
        return all([ pos != Belegung.FREI for pos in self._spielfeld.values()])

         
    def pruefe_auf_gewonnen(self, symbol):
        reihen = [
            (Pos.OBEN_LINKS, Pos.OBEN_MITTE, Pos.OBEN_RECHTS),
            (Pos.MITTE_LINKS, Pos.MITTE_MITTE, Pos.MITTE_RECHTS),
            (Pos.UNTEN_LINKS, Pos.UNTEN_MITTE, Pos.UNTEN_RECHTS),
            (Pos.OBEN_LINKS, Pos.MITTE_LINKS, Pos.UNTEN_LINKS),
            (Pos.OBEN_MITTE, Pos.MITTE_MITTE, Pos.UNTEN_MITTE),
            (Pos.OBEN_RECHTS, Pos.MITTE_RECHTS, Pos.UNTEN_RECHTS),
            (Pos.OBEN_LINKS, Pos.MITTE_MITTE, Pos.UNTEN_RECHTS),
            (Pos.OBEN_RECHTS, Pos.MITTE_MITTE, Pos.UNTEN_LINKS),
        ]
              
        for reihe in reihen:
            if all([ self._spielfeld[pos] == symbol for pos in reihe ]):
                return True
            
        return False
     
    def zustand(self):
        return self._zustand
    
    def laeuft(self):
        return self.naechster_zug() != None
 
    def naechster_zug(self):
        if self.zustand() == Zustand.KREUZ_IST_AM_ZUG:
            return Belegung.KREUZ
        elif self.zustand() == Zustand.KREIS_IST_AM_ZUG:
            return Belegung.KREIS
        return None 
    