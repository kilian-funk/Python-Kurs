"""
Aufgabe 3 aus http://projecteuler.net
(Deutsche Übersetzung auf http://projekteuler.de)

Größter Primfaktor

Die Primfaktoren von 13195 sind 5, 7, 13 und 29.

Was ist der größte Primfaktor der Zahl 600851475143?
"""


zahl = 600851475143

faktor = 2
while faktor <= zahl:
    if zahl%faktor == 0:
        zahl //= faktor
    else:
        faktor += 1


print("Groesster Primfaktor ist {}".format(faktor))
