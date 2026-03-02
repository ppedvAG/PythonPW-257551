# List
# Aufzählung von Daten
# Hält beliebig viele Daten (und beliebige Daten)
# Werden mit [ ] definiert
x = [1, 2, 3, 4]

print(x)

# Index
print(x[0])

print(x[-1])

print(x[2:4])

# append(Wert)
# Fügt einen Wert ans Ende der Liste an
# Syntax: list.append(Wert)
x.append(10)

print(x)

# pop(Index)
# Entfernt ein Element am gegebenen Index
# Syntax: list.pop(Index)
x.pop(3)

print(x)

# remove(Wert)
# Sucht einen Wert, und entfernt das erste Vorkommnis
# Syntax: list.remove(Wert)
x.remove(2)

print(x)

# sort()
# Sortiert die Liste
# Kann auch eine Richtung enthalten
# Syntax: list.sort()
x.append(6)
x.sort()

print(x)

x.sort(reverse=True)
print(x)

# extend(Andere Liste)
# Hängt zwei Listen aneinander
# Syntax: list.extend(list2)
y = [2, 3, 4]
x.append(y)

print(x)  # Verschachtelte Liste (nicht optimal)

x.remove(y)

x.extend(y)
print(x)

# Statt extend kann auch += verwendet werden
x += y
print(x)

########################################

# Tupel
# Liste, die aber nicht veränderbar ist
# Wird für Konstanten, Rückgabewerte, Parameter verwendet
t = (1, 2, 3)
print(t)

# Tupel über Umwege verändern
# -> Konvertierung
l = list(t)
l.append(4)
t = tuple(l)

print(t)

########################################

# range
# Bereich von X bis Y
# Syntax: range(X), range(X, Y), range(X, Y, Z)
r = range(10)  # Zahlen von 0-9 (Obergrenze exkludiert)

print(r)  # Nur ein Generator für Daten

# Um aus der Range Zahlen zu entnehmen, muss sie iteriert werden
print(list(r))

print(tuple(r))

for i in r:
	print(i)

print(list(range(10, 20)))  # 10-19

print(list(range(0, 1000, 20)))  # Range von X bis Y mit Schrittgröße

########################################

# Set
# Liste, bei dem jedes Element eindeutig sein muss
# Wird mit { } definiert
s = {1, 2, 3}
print(s)

s.add(3)  # Nichts passiert
print(s)

# Anwendung: Duplikate filtern
d = [1, 2, 2, 2, 3, 4, 4, 5]
print(set(d))

########################################

# dict
# Liste von eindeutigen Werden, aber jeder Wert hat eine Bezeichnung (Key)
auto = {
	"Marke": "VW",
	"Modell": "Golf",
	"Baujahr": "2020"
}

autoL = ["VW", "Golf", "2020"]  # Hier ist nicht klar, was die einzelnen Werte bedeuten

print(auto["Marke"])  # Werte auslesen
auto["KM"] = 10000  # Werte hineinschreiben (überschreibt, falls der Wert bereits existiert)

auto.setdefault("KM", 10000)  # Schreibt den Wert nur, wenn er noch nicht enthalten ist

# Listen, um das Dict zu untersuchen
auto.keys()
auto.values()
auto.items()

########################################

# Konvertierung
# Umwandlung von Variablen in andere Typen
# z.B.: int <-> float, list <-> tuple, ...
zahl1 = 5
zahl1 = float(zahl1)  # Wandle zahl1 zu einer Kommazahl um