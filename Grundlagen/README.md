
# Grundlagen in Python
https://www.python-lernen.de/python-grundlagen.htm

## Daten speichern mit Variablen
Programme verarbeiten Daten. Diese Daten können unterschiedlich geartet sein. Man sagt, sie haben einen bestimmten Typ.
### Einfache Datentypen
**Ganze Zahlen (int)**

**Gleitkommazahlen (float), entspricht rationalen Zahlen**: Diese haben eine Genauigkeit von ca. 15 Dezimalstellen.

**Wahrheitswerte (bool)**: Ein bool'scher Wert ist entweder wahr (`True`), oder falsch (`False`).

**Zeichenkette (string)**: Eine Zeichenkette ist eine beliebige lange Reihe an Zeichen, wie z. B. Buchstaben, Satzzeichen, Lehrzeichen oder sonstige Sonderzeichen. Jedes Zeichen wird intern durch einen bestimmten Zahlencode representiert.

### Kompexe Datentypen
**Liste (list)**: In einer Liste können bieliebig viele Daten in einer bestimmten Reihenfolge gespeichert werden. Über die Position in der Liste kann auf ein bestimmtes Element zugegriffen werden. Man kann Listen verwenden, um z. B. die gleiche Operation auf viele Daten anzuwenden. \
https://www.python-lernen.de/listen.htm

Es gibt noch eine Menge weiterer Datentypen, die wir uns zu einem späteren Zeitpunkt anschauen.

### Variablen
Daten können unter bestimmten Namen abgespeichert werden. Namen dürfen nur Groß- und Kleinbuchstaben und Unterstriche (_) enthalten. Mit einer Zuweisung werden die Daten dem Namen zugeordnet. So kann man später wieder darauf zugreifen.

```Python
meine_variable = 17
print(meine_variable)
```

## Programmablauf strukturieren
Mithilfe der folgenden Sprachelemente lässt sich der Programmablauf steuern. Damit sind nicht nur einfache Schritt-für-Schritt-Algorithmen möglich, sondern es können Verzweigungen oder Wiederholungen ausgedrückt werden.

**if-Bedingung** \
https://www.python-lernen.de/if-abfrage-python.htm

**while-Schleife** \
https://www.python-lernen.de/while-schleife.htm

**for-Schleife** \
https://www.python-lernen.de/for-schleife.htm


## Programmteile wiederverwenden durch Funktionen
Oft möchte man bestimmte Programmteile wiederverwenden, wie z. B. einen Suchalgorithmus. Hierfür nutzt man Funktionsdefinitionen. An einer Stelle wird der wiederzuverwendende Code definiert (Schlüsselwort def). Hierbei können auch Argumente festgelegt werden. Das sind Daten, die die Funktion benötigt, um richtig zu funktionieren. An anderer Stelle kann die Funktion dann aufgerufen werden.

Details unter:
http://www.python-lernen.de/funktionen-in-python.htm
