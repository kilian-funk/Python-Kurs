"""
Aufgabe 02: Binäre Suche

a)  Beschreibe in wenigen Sätzen, wie du in einem (großen) Speicher an
    sortierten Dingen ein bestimmtes Ding findest.

    Lösung:

    Wiederhole, solange mehr als ein Dinge im betrachteten Speicher ist:
        Nimm das Ding, das sich genau in der Mitte des betrachteten Speichers
        befindet (oder  bei gerader Anzahl das direkt oberhalb der Mitte).
        Ist das Ding kleiner oder gleich dem Gesuchten:
            dann betrachte nur noch die obere Hälfte des bisher betrachteten Speichers
            (inkl. der gewählten "Mitte"),
        Sonst:
            betrachte nur noch die untere Hälfte des bisher betrachteten Speichers
            (ohne die gewählte "Mitte").
    Gib es zurück --> Ende.
             

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
    mit zufälligem, aber sortiertem Inhalt erstellt.
    
    
d)  Ermittle für die Suche eines beliebigen Elements aus einer zufällig
    befüllten, sortierten Liste die durchschnittliche Anzahl an
    Such-Iterationen. Führe jeweils 10 Versuche durch. Vergleiche bei
    einer Listenröße von 10, 20, 40 und 80 Elementen.

"""

import math


def suche_binaer(liste, element):
    anfang = 0
    ende = len(liste)

    while ende-anfang > 1:
        mitte = math.floor((anfang+ende)/2)
        if liste[mitte] <= element:
            anfang = mitte
        else:
            ende = mitte
    return anfang
    

test_name = "Erstes Element"
print("Test {}: Start".format(test_name))

test_liste = [0, 5]
such_element = 0

such_index = suche_binaer(test_liste, such_element)

assert test_liste[such_index] == such_element, "test_liste[{}] ist {}, und nicht {}".format(
    such_index, test_liste[such_index], such_element)

print("{}[{}] == {}".format(test_liste, such_index, such_element))
print("Test {}: Ende".format(test_name))
print("*******************************************************")

test_name = "Zweites Element"
print("Test {}: Start".format(test_name))

test_liste = [0, 5]
such_element = 5

such_index = suche_binaer(test_liste, such_element)

assert test_liste[such_index] == such_element, "test_liste[{}] ist {}, und nicht {}".format(
    such_index, test_liste[such_index], such_element)

print("{}[{}] == {}".format(test_liste, such_index, such_element))
print("Test {}: Ende".format(test_name))
print("*******************************************************")

test_name = "n-tes Element"
print("Test {}: Start".format(test_name))

test_liste = [0, 3, 4, 7, 10, 15]
such_element = 10

such_index = suche_binaer(test_liste, such_element)

assert test_liste[such_index] == such_element, "test_liste[{}] ist {}, und nicht {}".format(
    such_index, test_liste[such_index], such_element)

print("{}[{}] == {}".format(test_liste, such_index, such_element))
print("Test {}: Ende".format(test_name))
print("*******************************************************")

# test_name = "Element nicht vorhanden"
# print("Test {}: Start".format(test_name))
# 
# test_liste = [5, 0, 9, 3, 7, 15]
# such_element = 16
# 
# such_index = None
# try:
#     such_index = suche_binaer(test_liste, such_element)
#     assert false, "Die Suche hat keinen Abbruch erzeugt"
# except ValueError:
#     pass
# 
# 
# print("{}[{}] == {}".format(test_liste, such_index, such_element))
# print("Test {}: Ende".format(test_name))
# print("*******************************************************")


# print("Ab hier Zusatzaufgaben...")

