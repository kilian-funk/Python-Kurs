from enum import Enum

class Pos(Enum):
    OBEN_LINKS = 0
    OBEN_MITTE = 1
    OBEN_RECHTS = 2
    MITTE_LINKS = 3
    MITTE_MITTE = 4
    MITTE_RECHTS = 5
    UNTEN_LINKS = 6
    UNTEN_MITTE = 7
    UNTEN_RECHTS = 8
    

class Belegung(Enum):
    FREI = 0
    KREIS = 1
    KREUZ = 2


class Zustand(Enum):
    OK = 0
    NICHT_ERLAUBT = -1
    KREUZ_GEWINNT = 1
    KREIS_GEWINNT = 2
    UNENTSCHIEDEN = 3
    KREIS_IST_AM_ZUG = 4
    KREUZ_IST_AM_ZUG = 5
    
    
class TicTacToe:
    
    def __init__(self, ausgabe):
        self._ausgabe = ausgabe
        self._ausgabe.zeichne_spielfeld()        
        self._spielfeld = { feld: Belegung.FREI for feld in Pos }
    
    def setze(self, pos, symbol):
        """ Setze ein Symbol (Belegung.KREUZ, Belegung.Kreis), wenn es die
        Spielregeln erlauben. Speichere die Belegung des Spielfeldes,
        rufe die entsprechende Ausgabe-Funktion auf und gib Zustand.OK oder
        Zustand.NICHT_ERLAUBT zurück.
        """
        return Zustand.OK
    
    def pruefe_auf_unentschieden(self):
        """
        Gibt True zurück, wenn die laufende Partie unentschieden zu ende
        gegangen ist.
        """
        return False
         
    def pruefe_auf_gewonnen(self, symbol):
        """
        Gibt True zurück, wenn das angefragte Symbol (Belegung.KREUZ oder
        Belegung.Kreis) gewonnen hat.
        """
        return False
     
    def zustand(self):
        """
        gibt zurück, in welchem Zustand sich das Spiel gerade befindet
        (ein Element von Zustand, z. B. Zustand.KREUZ_IST_AM_ZUG)
        """
        return Zustand.NICHT_ERLAUBT
    
    def laeuft(self):
        """ gibt True zurück, wenn das Spiel noch läuft, sonst False """
        return self.naechster_zug() != None
 
    def naechster_zug(self):
        """
        gib Zustand.KREUZ_IST_AM_ZUG oder Zustand.KREIS_IST_AM_ZUG
        oder None zurück
        """
        return None 
    