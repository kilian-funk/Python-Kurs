from turtle import *
import time
from tic_tac_toe_ansicht import *
from tic_tac_toe_modell import *

# Test 1: Passe die Ausgabe so an, dass ein Spielfeld mit Turtle gezeichnet wird
ansicht = Ansicht() 
ansicht.zeichne_spielfeld()
ansicht.zeichne_symbol(Pos.OBEN_LINKS, Belegung.KREUZ)
ansicht.zeichne_symbol(Pos.MITTE_LINKS, Belegung.KREIS)
ansicht.loesche_spielfeld()

# Test 2: Erweitere das Spiel-Modell, sodass es immer weis, wo welche Steine
# stehen und keine Felder doppelt belegt werden.
ansicht = Ansicht()
spiel = TicTacToe(ansicht)
assert spiel.setze(Pos.OBEN_LINKS, Belegung.KREUZ) == Zustand.OK
assert spiel.setze(Pos.OBEN_RECHTS, Belegung.KREIS) == Zustand.OK
assert spiel.setze(Pos.OBEN_LINKS, Belegung.KREUZ) == Zustand.NICHT_ERLAUBT

# Test 3: Erweitere das Spiel-Modell, sodass es auf die Reihenfolge achtet.
# (KREUZ beginnt immer)
ansicht = Ansicht()
spiel = TicTacToe(ansicht)
assert spiel.zustand() == Zustand.KREUZ_IST_AM_ZUG
assert spiel.setze(Pos.OBEN_LINKS, Belegung.KREUZ) == Zustand.OK
assert spiel.zustand() == Zustand.KREIS_IST_AM_ZUG
assert spiel.setze(Pos.OBEN_RECHTS, Belegung.KREUZ) == Zustand.NICHT_ERLAUBT
assert spiel.zustand() == Zustand.KREIS_IST_AM_ZUG
assert spiel.setze(Pos.OBEN_RECHTS, Belegung.KREIS) == Zustand.OK
assert spiel.zustand() == Zustand.KREUZ_IST_AM_ZUG
assert spiel.setze(Pos.OBEN_MITTE, Belegung.KREIS) == Zustand.NICHT_ERLAUBT
assert spiel.setze(Pos.UNTEN_LINKS, Belegung.KREUZ) == Zustand.OK

# Test 4: Erweitere das Spiel-Modell, sodass es den Sieger ermittelt
ansicht = Ansicht()
spiel = TicTacToe(ansicht)
assert spiel.setze(Pos.OBEN_LINKS, Belegung.KREUZ) == Zustand.OK
assert spiel.setze(Pos.MITTE_LINKS, Belegung.KREIS) == Zustand.OK
assert spiel.setze(Pos.OBEN_MITTE, Belegung.KREUZ) == Zustand.OK
assert spiel.setze(Pos.MITTE_MITTE, Belegung.KREIS) == Zustand.OK
assert spiel.setze(Pos.OBEN_RECHTS, Belegung.KREUZ) == Zustand.KREUZ_GEWINNT
assert spiel.zustand() == Zustand.KREUZ_GEWINNT


# Test 5: Schreibe einen Test, der den Zustand Unentschieden prüft



# Spiele eine Partie. Wie kannst du das Programm verbessern, dass es mit
# Fehleingaben besser umgehen kann?
ansicht = Ansicht()
spiel = TicTacToe(ansicht)

def spieler_eingabe(ansicht):
    return ansicht.position_aus_eingabe(input("Wo setzt du? "))

while (spiel.laeuft()):
    ansicht.berichte_zustand(spiel.zustand())
    eingabe = spieler_eingabe(ansicht)
    spiel.setze(eingabe, spiel.naechster_zug())
    
ansicht.berichte_zustand(spiel.zustand())
   

