# Schleifen
# Code mehrmals ausführen

# Zwei Varianten: while, for

# while
# Vom Aufbau identisch zu einer if-Bedingung, aber wird mehrmals ausgeführt

a = 0
b = 10
while a < b:  # Solange a kleiner als b ist, führe den Code darin aus
	print("a kleiner als b", a)
	a += 1

# Endlosschleife
# Schleife die für immer läuft
# Wird generell mit einem break abgebrochen
a = 0
b = 100
while True:  # "Bis-Schleife"
	print("Endlos")
	a += 1

	# break
	# Beendet die Schleife
	# Wird mit einer if kombiniert
	if a >= b:
		break  # Brich die Schleife ab

# continue
# Überspringe den Rest des jetztigen Schleifendurchlaufes
a = 0
b = 10
while True:  # "Bis-Schleife"
	print("Endlos")
	a += 1

	if a == 5:  # Ausnahmebedingungen definieren
		continue  # Wenn a == 5 ist, überspringe den Rest der Schleife
	print(a)

	if a >= b:
		break  # Brich die Schleife ab

# Praktisches Beispiel
emails = ["abc@def.de", "abcdef.de", "abc@def.de", "abcdef.de", "abc@def.de"]
c = 0
while c < len(emails):
	# Fehlerbehandlungscode
	e = emails[c]
	c += 1
	if "@" not in e:
		continue

	# Erfolgscode
	print("E-Mail Adresse valide:", e)

# else
# Wird nur ausgeführt, wenn die Schleife vollständig ausgeführt wird ohne break
while True:
	print("Hallo")
	break
else:
	print("Schleife vollständig ausgeführt")  # Wird hier nie ausgeführt

#######################################################

# for-Schleife
# Schleife, welche immer über eine Liste iteriert
# Wird oft mit einer Range kombiniert, um eine Zählerschleife zu bekommen

# Syntax: for <Variablenname> in <Liste>: ...
l = [1, 2, 3, 4, 5]
for x in l:
	print(x)  # x enthält immer den jetztigen Wert

# Umbau von E-Mail Schleife
emails = ["abc@def.de", "abcdef.de", "abc@def.de", "abcdef.de", "abc@def.de"]
for e in emails:  # e ist hier der string selbst (die jetztige Email)
	# Fehlerbehandlungscode
	if "@" not in e:
		continue

	# Erfolgscode
	print("E-Mail Adresse valide:", e)

# for-Schleife mit Range
for i in range(0, 10):
	print(i)

# Emails iterieren mit Range
for i in range(len(emails)):
	print(emails[i])

# fstring
# Formatted String
# Variablen in einen String einbetten, ohne mit + arbeiten zu müssen
text = "Gib eine Zahl ein: "
zahl = 3

# print(text + zahl)  # str und int können nicht mit + zusammengebaut werden
print(text + str(zahl))  # Hier muss zahl zu einem str konvertiert werden
print(f"{text}{zahl}")  # Alternative: fstring

print("Anzahl Emails: " + str(len(emails)))
print(f"Anzahl Emails: {len(emails)}")

anzEmails = f"Anzahl Emails: {len(emails)}"