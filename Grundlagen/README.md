
# Grundlagen in Python
https://www.python-lernen.de/python-grundlagen.htm

## Daten speichern mit Variablen
Programme verarbeiten Daten. Diese Daten können unterschiedlich geartet sein. Man sagt, sie haben einen bestimmten Typ.
### Einfache Datentypen
**Ganze Zahlen (`int`)**

**Gleitkommazahlen (`float`), entspricht rationalen Zahlen**: Diese haben eine Genauigkeit von ca. 15 Dezimalstellen.

**Wahrheitswerte (`bool`)**: Ein bool'scher Wert ist entweder wahr (`True`), oder falsch (`False`).

**Zeichenkette (`string`)**: Eine Zeichenkette ist eine beliebige lange Reihe an Zeichen, wie z. B. Buchstaben, Satzzeichen, Lehrzeichen oder sonstige Sonderzeichen. Jedes Zeichen wird intern durch einen bestimmten Zahlencode representiert.

### Kompexe Datentypen
**Liste (`list`)**: In einer Liste können bieliebig viele Daten in einer bestimmten Reihenfolge gespeichert werden. Über die Position in der Liste kann auf ein bestimmtes Element zugegriffen werden. Man kann Listen verwenden, um z. B. die gleiche Operation auf viele Daten anzuwenden. \
https://www.python-lernen.de/listen.htm

Es gibt noch eine Menge weiterer Datentypen, die wir uns zu einem späteren Zeitpunkt anschauen.

### Variablen
Daten können unter selbst gewählten Namen abgespeichert werden. Namen dürfen nur Groß- und Kleinbuchstaben, Ziffern und Unterstriche (_) enthalten. Mit einer Zuweisung werden die Daten dem Namen zugeordnet. So kann man später wieder darauf zugreifen.

```Python
meine_variable = 17
print(meine_variable)
```

## Arbeiten mit Fehlermeldungen

Fehlermeldungen helfen einem, Fehler zu beseitigen. Dafür musst du lernen, sie richtig zu lesen. Schauen wir uns ein Beispiel an:
```lang-non
Traceback (most recent call last):
  File "C:\Users\xxx\Desktop\Informatik\Python-Kurs\03_TicTacToe\tic_tac_toe.py", line 8, in <module>
    ansicht.zeichne_spielfeld()
  File "C:\Users\xxx\Desktop\Informatik\Python-Kurs\03_TicTacToe\tic_tac_toe_ansicht.py", line 8, in zeichne_spielfeld
    print(feld)
NameError: name 'feld' is not defined
```
Wir müssen die Meldung von unten nach oben lesen. In der letzten Zeile steht der eigentliche Fehler-Typ und was konkret schief gegangen ist. Unser Computer hat ein Problem mit einem Namen, hier "feld". Er kennt den Namen nicht. In der Zeile darüber steht der Befehl, der den Fehler ausgelöst hat, hier "print(feld)".

Darüber ist genau die Stelle bezeichnet, wo der Fehler aufgetreten ist, Datei und Zeile. Wenn der Fehler in einer Funktion aufgetreten ist, die von einer anderen Funktion aufgerufen wurde, steht die Stelle der aufrufenden Funktion noch darüber. So lässt sich rekonstruieren, wie es zu dem Fehler gekommen ist.

Versuche die Fehlermeldungen genau zu lesen. Wenn du die englischen Begriffe nicht verstehst, nimm dir ein Wörterbuch zu Hilfe.

## Programmablauf strukturieren
Mithilfe der folgenden Sprachelemente lässt sich der Programmablauf steuern. Damit sind nicht nur einfache Schritt-für-Schritt-Algorithmen möglich, sondern es können Verzweigungen oder Wiederholungen ausgedrückt werden.

**if-Bedingung** \
https://www.python-lernen.de/if-abfrage-python.htm

**while-Schleife** \
https://www.python-lernen.de/while-schleife.htm

**for-Schleife** \
https://www.python-lernen.de/for-schleife.htm


### Programmteile wiederverwenden durch Funktionen
Oft möchte man bestimmte Programmteile wiederverwenden, wie z. B. einen Suchalgorithmus. Hierfür nutzt man Funktionsdefinitionen. An einer Stelle wird der wiederzuverwendende Code definiert (Schlüsselwort `def`). Hierbei können auch Argumente festgelegt werden. Das sind Daten, die die Funktion benötigt, um richtig zu funktionieren. An anderer Stelle kann die Funktion dann aufgerufen werden.

Details unter:
http://www.python-lernen.de/funktionen-in-python.htm

### Daten und Funktionen zusammenfassen in Klassen
Mit Klassen lassen sich Daten und dazugehörige Funktionen zusammenfassen. Dies ist ein komplexes und leistungsfähiges Konzept aus der object-orientierten Programmierung (OOP).

Details unter:
https://www.python-lernen.de/klassen-in-python.htm

### Weitere Datentypen

**Wörterbuch (`dict`)**: In einem Wörterbuch werden Daten jeweils zu einem Schlüssel gespeichert. In einer Liste ist die Position der Schlüssel zu einem bestimmten Datum und in einem Wörterbuch ist es z. B. ein Schlüsselwort. Beispiel:

```Python
woerterbuch = {
    'null': 'zero',u
    'eins': 'one',
    'zwei': 'two',
    'drei': 'three'
}
```
Ein Wert kann ähnlich wie bei einer Liste abgerufen werden.

Details unter:
https://www.python-lernen.de/python-dictionary.htm


**Aufzählungen (Enum)**: Mit einer Aufzählung kann man Begriffe festlegen, die einem helfen, Dinge durchzuzählen. Schauen wir uns ein Beispiel an:

```Python
class Belegung(Enum):
    FREI = 0
    KREIS = 1
    KREUZ = 2
```
Diese Begriffe können verwendet werden, wenn verschiede Programmteile zusammenarbeiten.
```Python
setze_spielfigur(Belegung.KREIS)
```

## Benutzer Ein-/Ausgabe

Die Ein- und Ausgabe an den Benutzer ist ein wichtiges Thema, um ein sinnvolles Computerprogramm zu erstellen.
Es gibt verschiedene Möglichkeiten.

### Einfache Text-Ein-/Ausgabe
Die einfachste Möglichkeit ist eine einfache Text-Eingabe:
```Python
name = input("Wie heisst Du? ")
alter = int(input("Wie alt bist Du? "))
```
Damit wird der Benutzer aufgefordert, eine Eingabe zu machen. Der eingegebene Text wird in der Variablen `name` gespeichert. Wenn kein Text, sondern eine Zahl eingegeben werden soll, dann muss der Text noch entsprechend umgewandelt werden (s. zweite Zeile im obigen Beispiel mit der Variablen `alter`).
Eine einfache Ausgabe kann mit dem `print`-Befehl erfolgen:
```Python
print("Dies ist eine Ausgabe.")
print("Du heisst {} und bist {} Jahre alt".format(name, alter))
```
In der ersten Zeile wird nur ein Text ausgegeben. In der zweiten Zeile werden vor der Ausgabe zwei Textstellen mit Variablen-Werten ersetzt.

### Grafische Benutzer-Ein-/Ausgabe
Die meisten größeren Computerprogramme haben grafische Benutzerschnittstellen. Dafür gibt es spezielle Bibliotheken. Hier verwenden wir die `Turtle`-Bibliothek. Damit können einfache Bilder gezeichnet werden und Ereignisse wie Maus-Klicks verarbeitet werden.

Eine Einführung dazu findest du hier:
https://www.python-lernen.de/python-turtle.htm

## Aufbau von Programmen

### E V A : Eingabe - Verarbeitung - Ausgabe

Einfache Aufgaben werden nach diesem Prinzip aufgebaut.

* Die drei Phasen des Programms laufen nacheinander ab
  * **Eingabe:** hier werden alle nötigen Informationen gesammelt, entweder durch Benutzereingabe, Einlesen einer Datei oder Netzwerkübertragung, ...
  * **Verarbeitung:** Die Daten werden zu einem Ergebnis verarbeitet.
  * **Ausgabe:** Das Ergebnis wird ausgegeben, auf den Bildschirm, eine Datei, den Drucker
  oder eine Netzwerkverbindung.
* Das Ende des Programms ist eindeutig.

**Beispiel: Anfrage an Wikipedia.**
* Eingabe: Der Wikipedia-Server erhält eine Anfrage nach einem Artikel. Die Seite wird von einer Datenbank geladen.
* Verarbeitung: Der Artikel wird formatiert.
* Ausgabe: Die erstellte Web-Seite wird über die Netzwerkverbindung zurückgeschickt.


### M V C: Model - View - Controller

Größere Programme, die eine grafische Benutzeroberläche haben und flexibel auf Nutzereingaben reagieren müssen, werden oft mit diesem Modell aufgebaut. Der Name ist englisch und kann mit "Modell, Ansicht, Steuerer" übersetzt werden. Die drei Teile (MVC) des Programms sind dabei nicht Phasen, die nach einander ablaufen, sondern während des gesammten Ablaufs eine bestimmte Aufgabe wahrnehmen:
* **Modell (Model):** Der Modell-Teil enthält alle wichtigen Daten des Programms und weiss, wie sie bearbeitet werden können.
* **Ansicht (View):** Der Ansichts-Teil übernimmt die Darstellung auf dem Bildschirm und definiert die Eingabemöglichkeiten.
* **Steuerer (Controller):** Der Steuerer ist das eigentliche Hauptprogramm, dass zu Beginn alle Programmteile aufbaut, alle Verbindungen zwischen den Programmteilen herstellt und am Ende wieder alles aufräumt.

**Beispiel: Schachcompter.**
* Modell: Enthält die Informationen zum Spielzustand, z. B. wer ist am Zug, welche Figuren stehen auf welchem Feld (z. B. schwarzer Bauer auf D4), alle Spielregeln (z. B. darf der Bauer von D4 auf D5 ziehen?).
* View: Zeichnet das Spielfeld und die Figuren auf den Bildschirm. Hier wird entschieden, ob es eine 3D-Ansicht ist, oder nur einfache Symbole. Hier werden auch Benutzereingaben erfasst, aber nicht vollständig verarbeitet (z. B. der Benutzer zieht eine Figur von einem Feld auf ein anderes). Für die vollständige Verarbeitung ist das Wissen aus dem Modell nötig.
* Controller: Baut das Spiel auf (Modell und View) und verbindet alles miteinander. Z. B. müssen sich Ansichtsteil und Modell verständigen, ob ein Zug erlaubt ist. Diese Verbindungen zwischen beiden werden vom Steuerer aufgebaut.
