"""
Aufgabe 01: Lineare Suche

a)  Beschreibe in wenigen Sätzen, wie du in einem (großen) Speicher mit
    unsortierten Dingen ein bestimmtes Ding findest.

    Lösung:

    Nimm der Reihe nach alle Dinge:
        Wenn das das Ding mit dem gesuchten übereinstimmt:
            Gib es zurück --> Ende.
    Das gesuchte Ding ist nicht in der Liste --> Abbruch.


b)  Schreibe eine Funktion, die den Algorithmus von a) für Zahlen in einer
    Liste erfüllt.
    Die Funtion soll zwei Argumente nehmen (Liste an Daten, gesuchtes Element)
    und die Position des gesuchten Elements in der Liste (index) zurück geben.
    Benutze dazu die Tests, um nach und nach alle Fälle abzudecken.


Zusatzaufgabe:

c)  Erweitere die Funktion, sodss sie nicht nur die Position des gesuchten
    Elements, sondern auch die Anzahl an benötigten Such-Iterationen in einer
    globalen Variablen gespeichert wird.


d)  Schreibe eine Funktion, die für eine bestimmte Listengröße eine Liste
    mit zufälligem Inhalt erstellt.
    
    
d)  Ermittle für die Suche eines beliebigen Elements aus einer zufällig
    befüllten Liste die durchschnittliche Anzahl an Such-Iterationen. Führe
    jeweils 10 Versuche durch. Vergleiche bei einer Listenröße von 10, 20, 40
    und 80 Elementen.

"""

import random

such_iterationen = 0

def suche_linear(liste, element):
    global such_iterationen
    such_iterationen = 1
    
    for index in range(len(liste)):
        if liste[index] == element:
            return index
        such_iterationen += 1
        
    raise ValueError("{} ist nicht in der Liste".format(element))


test_name = "Erstes Element"
print("Test {}: Start".format(test_name))

test_liste = [5, 0]
such_element = 5

such_index = suche_linear(test_liste, such_element)

assert(test_liste[such_index] == such_element)

print("{}[{}] == {}".format(test_liste, such_index, such_element))
print("Test {}: Ende".format(test_name))
print("*******************************************************")

test_name = "Zweites Element"
print("Test {}: Start".format(test_name))

test_liste = [5, 0]
such_element = 0

such_index = suche_linear(test_liste, such_element)

assert(test_liste[such_index] == such_element)

print("{}[{}] == {}".format(test_liste, such_index, such_element))
print("Test {}: Ende".format(test_name))
print("*******************************************************")

test_name = "n-tes Element"
print("Test {}: Start".format(test_name))

test_liste = [5, 0, 9, 3, 7, 15]
such_element = 7

such_index = suche_linear(test_liste, such_element)

assert(test_liste[such_index] == such_element)

print("{}[{}] == {}".format(test_liste, such_index, such_element))
print("Test {}: Ende".format(test_name))
print("*******************************************************")

test_name = "Element nicht vorhanden"
print("Test {}: Start".format(test_name))

test_liste = [5, 0, 9, 3, 7, 15]
such_element = 16

such_index = None
try:
    such_index = suche_linear(test_liste, such_element)
except ValueError:
    pass

print("{}[{}] == {}".format(test_liste, such_index, such_element))
print("Test {}: Ende".format(test_name))
print("*******************************************************")


print("Ab hier Zusatzaufgaben...")

def erzeuge_test_liste(anzahl, groesse):
    return random.sample(list(range(groesse)), anzahl)

def waehle_element_aus_liste(liste):
    return random.choice(liste)

def durchschnitt_anzahl_iterationen(anzahl_daten,
                                    maximale_groesse, anzahl_versuche):
    anzahl_iterationen = 0
    for _ in range(anzahl_versuche):
        test_daten = erzeuge_test_liste(anzahl_daten, maximale_groesse)
        suche_linear(test_daten, waehle_element_aus_liste(test_daten))
        anzahl_iterationen += such_iterationen
    return anzahl_iterationen/anzahl_versuche

_anzahl_versuche = 10
_groesse_der_zahlen = 100000

print("Durchschnittliche Anzahl an Iterationen bei verschieden Listengrößen")
print({i:durchschnitt_anzahl_iterationen(i, _groesse_der_zahlen,
                                         _anzahl_versuche)
                                for i in [10, 20, 40, 80]})

