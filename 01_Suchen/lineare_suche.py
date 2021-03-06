"""
Aufgabe 01: Lineare Suche

a)  Beschreibe in wenigen Sätzen, wie du in einem (großen) Speicher an
    unsortierten Dingen ein bestimmtes Ding findest.

    Lösung:

    ...


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
    # Lösung für Aufgabe b) kommt hier rein
    pass


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

