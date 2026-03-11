# Kommentare
# Text der nicht ausgeführt wird
# Es gibt den #-Kommentar oder den docstring (""")

print("Hallo Welt")  # Können auch am Ende einer Zeile zu stehen

############################################

# Variablen
# Speicher für Inhalte/Daten
# WICHTIG: Der Inhalt einer Variable bestimmt den Typen der Variable
# D.h.: Anhand eines Variablennamens kann niemals festgestellt werden, was sich in der Variable befindet

# Variable definieren
# Syntax: <Name> = <Wert>
x = 5  # Variable mit int Inhalt

# int
# Ganze Zahl
# Hat keine Größenbeschränkung
z = 132897582386587329157643278953125476814935276384253674893675
print(z)

# float
# Kommazahl
# Hat keine Größenbeschränkung
f = 218_572_390_859_234_867_523_490_567_231_459.32578943265892465897264587294658732465  # Trennzeichen
print(f)

# str (String)
# Text/Zeichenkette
# Muss mit einzelnen oder doppelten Hochkomma definiert werden (' ', " ")
text = "Ich bin ein Text"
print(text)

text2 = 'Ich bin ein Text'
print(text2)

# bool
# Wahr-/Falschwert
b1 = True
b2 = False

# complex
# Komplexe Zahlen
c = 5 + 12j
print(c)

############################################

# Index
# Einzelnes Element aus einer Liste entnehmen
print(text[0])  # Das erste Element

print(text[-1])  # Das letzte Element

print(text[3:6])  # Bereichsindex, Obergrenze exkludiert

print(text[:6])  # Bis 6, Untergrenze wird ergänzt

print(text[3:])  # Von 3, Obergrenze wird ergänzt

print(text[:])  # Alles

############################################

# Stringfunktionen
# Operationen auf einem gegeben String durchführen
# Hier wird der Punkt-Operator benötigt

# count
# Zählt die Vorkommnisse von einem Zeichen
anzahl = text.count("T")  # 1, nicht in der Konsole sichtbar
print(anzahl)

print(text.count("T"))

# lower(), upper()
# Konvertieren alle Zeichen in kleinbuchstaben oder GROßBUCHSTABEN
# WICHTIG: Alle Funktionen lassen die originale Variable immer unberührt
print(text.lower())
print(text.upper())

# Aufgabe: Alle t's Zählen unabhängig ob groß/klein
print(text.count("T") + text.count("t"))
print(text.lower().count("t"))
print(text.upper().count("T"))

# islower(), isupper()
# Prüft, ob der gesamte String lowercase oder UPPERCASE ist
print(text.islower())

# Einzelne Zeichen prüfen
print(text[0].isupper())

# capitalize(), title()
# Macht das erste/alle Anfangsbuchstaben groß
print(text.title())
print(text.capitalize())

# len
# Gibt die Länge einer Liste zurück
# Wird für alle Listen in Python verwendet
print(len(text))  # 16 Zeichen

############################################

# Arithmetik
# +, -, *, /

zahl1 = 4
zahl2 = 7

zahl1 + zahl2  # Dieses Statement berechnet nur die Summe (zahl1 bleibt unverändert)

zahl1 += zahl2  # Dieses Statement addiert zahl1 auf zahl2 hinauf (zahl1 wird verändert)

zahl1 = zahl1 + zahl2  # Selbes Statement wie darüber

print(zahl1 + zahl2)  # Nur das Ergebnis berechnen

# Division
# Bei einer Division kommt auch eine Kommazahl zurück (nicht Standard in der Programmierung)
print(3 / 5)  # 0.6

# Ganzzahldivision
print(3 // 5)  # Schneidet die Kommastellen ab

# Modulo
# Rest einer Division
print(8 % 5)  # 3

print(12 % 5)  # 2

# Potenzoperator
# X^Y
print(3 ** 3)  # 27

print(5 ** -1)  # 1/5

print(9 ** 0.5)  # Wurzel: 3

# Addition mit Strings
t1 = "Hallo"
t2 = "Welt"

print(t1 + " " + t2)

t1 += " " + t2
print(t1)

# Strings multiplizieren
print(t1 * 10)