# Lambda
# Anonyme Funktionen
# D.h., Funktionen die nicht per def definiert werden, sondern einmalig in eine Variable geschrieben werden
# Dadurch sind diese Funktionen nicht wiederverwendbar, und werden nach Verwendung weggeworfen
def halloWelt():
	print("Hallo Welt")

halloWelt()  # Diese Funktion kann jetzt überall verwendet werden

x = halloWelt  # Hier wird jetzt ein Funktionszeiger gespeichert
print(x)  # Über x kann jetzt auf die Funktion zugegriffen werden, ohne den originalen Namen zu kennen

x()  # halloWelt() ausführen

l = lambda: print("Hallo Welt")  # Funktion direkt in Variable legen ohne def zu Verwenden
l()

###############################################

# filter, map

# filter
# Filtert eine Liste anhand einer Bedingung
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9]

durch2 = []
for x in zahlen:
	if x % 2 == 0:
		durch2.append(x)

def teilbarDurch2(x: int):
	return x % 2 == 0

# Hier wird eine Schleife im Hintergrund ausgeführt
# Bei jedem Element wird die Funktion ausgeführt, wenn diese True zurückgibt, kommt die jetztige Zahl in die Ergebnismenge hinein
y = filter(teilbarDurch2, zahlen)
print(list(y))

z = filter(lambda x: x % 2 == 0, zahlen)
print(list(z))

# map
# Transformiert jedes Element der Liste in eine neue Form

# Aufgabe: Jede Zahl ** 2
# Hier wird eine Schleife im Hintergrund ausgeführt
# Bei jedem Element wird die Funktion ausgeführt, die jetztige Zahl kommt in ihrer neuen Form in die Ergebnismenge hinein
h = map(lambda x: x ** 2, zahlen)  # Neue Form: x ** 2
print(list(h))

# Siehe LC (M006)

# LL        CCCCC     M     M    00000     00000      66666
# LL      CC     CC   MM   MM   00   00   00   00    66
# LL     C         C  M M M M  00     00 00     00  66
# LL     C            M  M  M  00     00 00     00  66666
# LL     C         C  M     M  00     00 00     00  66   66
# LL      CC     CC   M     M   00   00   00   00   66   66
# LLLLLL     CCCCC    M     M    00000     00000     66666