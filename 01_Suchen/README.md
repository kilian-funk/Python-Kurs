# Suchen in großen Datenmengen

## Wichtige Begriffe

### Algorithmus
Präzise Vorschrift, wie eine Reihe an Tätigkeiten durchzuführen ist, um ein bestimmtes Ergebnis oder Ziel zu erreichen. Die Anweisungen müssen für den oder die Ausführende verständlich und eindeutig sein. Die Reihenfolge der Anweisungen ist von Bedeutung. Es können auch Schleifen oder Fallunterscheidungen verwendet werden.

Ein Beispiel für einen Algorithmus ist ein Kochrezept.

### Lineare Suchen
Sind die Daten, in denen gesucht wird unsortiert, so bleibt nur die lineare Suche. Bei der linearen Suche wird ein Element nach dem anderen betrachtet, solange bis das gesuchte Element gefunden wird. Es werden zwischen 1 und _n_ Versuchen benötigt, wenn _n_ die Anzahl an Elementen ist.

### Binäre Suche (oder Suche durch Bisektion)
Sind die Daten, in denen gesucht wird sortiert, so kann die binäre Suche angewandt werden. Dabei betrachtet man zunächst das Element, daß genau in der Mitte der gesamten Daten liegt. Ist dieses Element größer als das Gesuchte, kann die hintere Hälfte der Daten verworfen werden. Ist das Element dagegen kleiner als das Gesuchte, kann die vordere Hälfte verworfen werden. Damit kann die Menge der Daten, in denen gesucht wird bei jedem Schritt halbiert werden.

Bisektion ist ein wichtiges Konzept in der Informatik, bei dem ein großes Problem in mehrere kleinere Probleme zerlegt wird. Dieser Schritt wird solange wiederholt, bis die verbleibenden Probleme einfach zu lösen sind.

Ein Problem durch Bisektion zu lösen, ist oft sehr effizient.

### Mittelwert
Der Mittelwert ist ein Begriff aus der Statistik. Er bezeichnet eine zentrale Tendenz einer Verteilung (z. B. von Messwerten). Der Mittelwert ist ein wichtiges Werkzeug, um den Aufwand von Algorithmen zu bestimmen. Wenn man einen Versuch _n_ mal durchführt, dann bekommt man n Ergebnisse _x_<sub>1</sub>, _x_<sub>2</sub>, ..., _x<sub>n</sup>_.
Der Mittelwert ist dann

  x_quer = (_x_<sub>1</sub> + _x_<sub>2</sub> + ... + _x<sub>n</sub>_) / _n_
