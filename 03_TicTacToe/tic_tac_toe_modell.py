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
    