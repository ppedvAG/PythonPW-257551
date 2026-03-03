# Anweisungen

# if-Anweisung
# Code nur ausführen, wenn eine bestimmte Bedingung gegeben ist
# Wird übersprungen, wenn die Bedingung nicht gegeben ist

z1 = 5
z2 = 8

if z1 > z2:  # Hier muss ein Doppelpunkt gemacht werden
	print("Zahl1 ist größer als Zahl2")  # WICHTIG: Einrückungen beachten
print("Nach der if")  # Ohne Einrückung wird dieser Codeblock immer ausgeführt (unabhängig von der if-Bedingung)

# elif, else
# Alternative Bedingungen in Kombination mit der if
# Werden immer statt der if ausgeführt (wenn sie ausgeführt werden)

if z1 > z2:
	print("Zahl1 ist größer als Zahl2")
else:  # Wenn z1 nicht größer als z2 ist (beinhält auch z1 == z2)
	print("Zahl1 kleiner oder gleich Zahl2")

# elif
if z1 > z2:
	print("Zahl1 ist größer als Zahl2")
elif z1 == z2:
	print("Zahl1 gleich Zahl2")
else:
	print("Else erreicht")
	print("Zahl1 kleiner Zahl2")

# Vergleichsoperatoren
# ==, !=
# <, >=
# >, <=

# Logische Operatoren
# and, or, not
# in, is

# and
# Bedingungen verbinden
if z1 > z2 and z1 > 5:  # Beide Bedingungen müssen gültig sein
	print("...")

if z1 > z2 & z1 > 5:  # Beide Bedingungen müssen gültig sein
	print("...")

# or
# Bedingungen verbinden
if z1 > z2 or z1 > 5:  # Eine von beiden Bedingungen (oder beide) müssen gültig sein
	print("...")

if z1 > z2 | z1 > 5:  # Eine von beiden Bedingungen (oder beide) müssen gültig sein
	print("...")

# not
# Bedingungen invertieren
text = "Hallo Welt"
if not text.isnumeric():  # text nicht numerisch
	print("...")

if not (z1 > z2 and z1 > 5):  # not invertiert einen gesamten Block
	print("...")

if z1 <= z2 or z1 <= 5:  # if-Bedingung logisch invertiert (ohne den not-Operator)
	print("...")

# in
# Prüft, ob eine Liste ein gegebenes Element enthält
# Kann auch mit not kombiniert werden
# Wird auch Contains genannt
l = [1, 2, 3, 4]

if 3 in l:
	print("3 ist in l enthalten")

if 3 not in l:
	print("...")

if "A" in text:
	print("text enthält mind. ein A")

# Eingabe zw. 1 und 4 prüfen
eingabe = "1"
optionen = ["1", "2", "3", "4"]

if eingabe in optionen:
	print("Eingabe ist valide")
else:
	print("Bitte neue Eingabe zw. (inklusive) 1 und 4 machen")

# Ternary Operator
# if-elif-else verbinden in einer Zeile
# Kompakt, aber unleserlich
if z1 > z2:
	print("Zahl1 ist größer als Zahl2")
elif z1 == z2:
	print("Zahl1 gleich Zahl2")
else:
	print("Zahl1 kleiner Zahl2")

# Das else ist hier der Separator
# Kein elif
print("Zahl1 ist größer als Zahl2") if z1 > z2 else print("Zahl1 gleich Zahl2") if z1 == z2 else print("Zahl1 kleiner Zahl2")

print("Zahl1 ist größer als Zahl2") if z1 > z2 \
	else print("Zahl1 gleich Zahl2") if z1 == z2 \
	else print("Zahl1 kleiner Zahl2")

print("Zahl1 ist größer als Zahl2" if z1 > z2 else "Zahl1 gleich Zahl2" if z1 == z2 else "Zahl1 kleiner Zahl2")