"""

Jeder neue Term in der Fibonacci-Reihe wird gebildet, indem die beiden
vorherigen Zahlen addiert werden. Wenn man mit 1 und 2 beginnt, sind die
ersten 10 Terme wie folgt:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Finden Sie die Summe aller geraden Terme der Fibonacci-Reihe,
die 4 Millionen nicht überschreiten.

"""

grenze = 4_000_000

# 1. Lösung: Schleife über alle Fibonacci-Zahlen kleiner 4 Millionen.
# Summiere alle geraden Fibonacci-Zahlen auf
summe = 0
f_vor, f = 1, 2

while f<= grenze:
    if f % 2 == 0:
        summe += f
    f_vor, f = f, f_vor + f

print(summe)

# 2. Lösung: Definiere einen Generator für Fibonacci-Zahlen kleiner max.
# Summiere über Generator-Comprehension mit Filter
def fibonacci(max):
    f_vor, f = 1, 1
    while f<= max:
        yield f
        f_vor, f = f, f_vor + f

summe = sum(f for f in fibonacci(grenze) if f %2 == 0)

print(summe)
