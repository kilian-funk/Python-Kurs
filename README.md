# Python-Kurs
Dieses Projekt enthält Unterlagen für einen Informatik-Kurs aufbauend auf geringem Vorwissen.

## Hilfreiche Links
### Python-Einführung

https://www.python-lernen.de/\
https://py-tutorial-de.readthedocs.io/de/python-3.3/ \
https://www.python-kurs.eu/python3_kurs.php

### Entwicklungsumgebung

**IDLE** -
Pythons Integrierte Entwicklungs- und Lern-Umgebung (Teil des Python-Pakets): https://python.org/downloads

**Thonny** - Einfache Entwicklungsumgebung auf Deutsch:
https://thonny.org

## Wichtige Begriffe zu Python

### Code-Block
Ein Code-Block ist ein Programmstück, dass durch eine Einrückung besonders gekennzeichnet wird, und dass angibt, welche Code-Zeilen als Einheit betrachtet werden sollen. Meisst wird ein Code-Block durch eine Zeile mit Doppelpunkt eingeleitet (Beispiel: siehe Schlüsselwort "def"). Durch verschiedene Einrückungen können Code-Blöcke geschachtelt werden.

### Schlüsselwörter
Schlüsselwörter, die in der Programmiersprache Python eine besondere und wichtige Bedeutung haben. Sie sind fest in die Sprache eingebaut und dienen oft dazu Strukturen wie Schleifen oder Verzweigungen auszudrücken. Im Folgenden findest du einige wichtige Schlüsselwörter:

**import und from**\
Mit diesen Schlüsselwörtern gibt man an, dass eine Bibliothek oder eine Funktion oder Modul einer Bibliothek verwendet werden soll. Beispiel:
```Python
import random
```

**def**\
Definiert eine Funktion. Dadurch kann man bestimmte Programmteile wiederverwendbar machen. Beispiel

```Python
def mal_zwei(zahl):
    zahl_mal_zwei = 2 * zahl
    return zahl_mal_zwei
```

**return**\
Gibt an, dass eine Funktion an dieser Stelle verlassen wird. Es kann optional ein Rückgabeargument verwendet werden. (Beispiel: siehe "def")

**for ... in ...:**\
Definiert eine Schleife mit vorgegebenen Wiederholungen. Beispiel:

```Python
for i in [0, 1, 2, 3]:
  print(i)
```
Die Variable i nimmt der Reihe nach alle Werte aus der Liste [0,1,2,3] an. Damit wird dann der Block nach dem Doppelpunkt ausgeführt.

**while ...:**\
Definiert eine Schleife, bei der vor jedem Durchlauf eine Bedingung geprüft wird.

```Python
while random.randint(1,6) >= 3:
  print("Du hast eine 3 oder größer gewürfelt")
```

**break**\
Beendet eine Schleife sofort. Das Programm wird nach der Schleife fortgesetzt.

**if ...: ... else:**\
Verzweigung im Programmfluss. Es wird eine Bedingung ausgewertet und dann einer von zwei Code-Blöcken ausgeführt. Der zweite Code-Block ist dabei optional. Beispiel:

```Python
if a < 5:
  print("a ist kleiner als 5")
else:
  print("a ist groeßer oder gleich 5")
```

**raise** \
Löst eine Ausnahme aus.
