"""
Aufgabe 1 aus http://projecteuler.net
(Deutsche Übersetzung auf http://projekteuler.de)

Wenn wir alle natürlichen Zahlen unter 10 auflisten, die Vielfache von 3
oder 5 sind, so erhalten wir 3, 5, 6 und 9. Die Summe dieser Vielfachen ist 23.

Finden Sie die Summe aller Vielfachen von 3 oder 5 unter 1000.
"""

# Einfach, aber nicht schön
summe = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        summe += i
print(summe)

# Kompakt und elegant mit "list comrehensions"
summe = sum([i for i in range(1,1000) if i % 3 ==0 or i % 5 == 0])
print(summe)

# Auch sehr elegant mit der Vereinigung von Mengen
summe = sum(set(range(0,1000,3))|set(range(0,1000,5)))
print(summe)

# Das ist in funktionalen Sprachen die "klassische" Lösung
import functools
summe = functools.reduce(lambda x,y: x+y,
                         filter(lambda x: x % 3 == 0 or x % 5 == 0,
                                range(1,1000)))
print(summe)
