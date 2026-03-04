# Funktionen
# Code wiederverwenden
# -> Code in Funktionen speichern, und diese später verwenden

# def
# Legt eine neue Funktion an
# Syntax: def <Name>(<Parameter>): ...
def hallo():
	print("Hallo Welt")

hallo()  # Der Code innerhalb von hallo() wird hier ausgeführt
hallo()
hallo()

############################################

# Parameter
# Funktionen Daten mitgeben
# Beliebig viele Variablennamen in der Klammer definieren
def hallo(name):
	print(f"Hallo {name}!")  # Je nach Parameter hat der Aufruf dieser Funktion verschiedene Asuswirkungen

hallo("Lukas")
hallo("Björn")

def addieren(x, y):
	print(f"{x} + {y} = {x + y}")

addieren(3, 3)

# Großer Nachteil: Parameter in Python können beliebige Daten empfangen
# Wir können den User nicht abhalten, beliebige fehlerhafte Daten einzugeben
addieren(3, 4)
addieren(3.4, 9.2)
addieren("Hallo", "Welt")
addieren([1, 2, 3], [4, 5, 6])  # Hier sind beliebige Daten erlaubt

############################################

# Typempfehlung
# Bei Parametern den gewünschten Typen angeben
# WICHTIG: User kann weiterhin beliebige Daten eingeben
def addieren2(x: int, y: int):
	print(f"{x} + {y} = {x + y}")

addieren2(3, 4)
addieren2(3.4, 9.2)  # Expected type 'int', got 'float' instead

def addieren3(x: int | float, y: int | float):
	print(f"{x} + {y} = {x + y}")

addieren3(4, 2)
addieren3(8.5, 3)

# Typvergleich
# Prüft per if, ob die Variable tatsächlich den korrekten Typen hat
# "Streng"
def addieren4(x: int | float, y: int | float):
	if type(x) in [int, float] and type(y) == int:
		print(f"{x} + {y} = {x + y}")
	else:
		raise TypeError("X und Y müssen Integer sein!")  # raise: Lässt das Programm abstürzen

addieren4(3.4, 3)

############################################

# Rückgabewerte
# Ergebnis bei einer Funktion zurückgeben
# Dieses Ergebnis kann in eine Variable geschrieben werden und weiterverarbeitet werden
text = "Ich bin ein Text"
s = text.split(" ")  # Rückgabewert: list[str]
u = text.upper()  # Rückgabewert: str

def addieren5(x: int, y: int):
	return x + y  # Gibt das Ergebnis zurück
	# print("Hallo")  # WICHTIG: return bricht die Funktion ab (beendet die Funktion)

summe = addieren5(4, 9)  # Ergebnis sollte hier in einer Variable gefangen werden

print(f"Summe: {summe}")

# Funktion mit mehreren Rückgabewerten
# Hier wird generell ein Tupel verwendet
def rechenarten(x: int, y: int):
	return (x + y, x - y, x * y, x / y)

t = rechenarten(3, 4)
print(t)

# Typempfehlung bei Rückgabewert
# Erkennt PyCharm generell von selbst (nicht notwendig)
def halloWelt() -> str:
	return "Hallo Welt"

print(halloWelt())

############################################

# Default Arguments
# Parameter können Standardwerte bekommen
# Diese können überschrieben werden, oder auch nicht
def addieren6(x: int, y: int = 0):
	return x + y

print(addieren6(3, 4))
print(addieren6(8))

# Funktionen konfigurieren
# In Python gibt es sehr viele Funktionen, die 10, 20, 50, ... Parameter haben
# Fast alle (oder alle) diese(r) Parameter sind optional
# Über den Namen des Parameters kann dann genau dieser verändert
# Es müssen nicht alle Parameter angegeben werden, sondern nur die benötigten

# Beispiel: pandas.read_csv
# pandas.read_csv(filepath_or_buffer, *, sep=<no_default>, delimiter=None, header='infer', names=<no_default>, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, skip_blank_lines=True, parse_dates=None, date_format=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, on_bad_lines='error', low_memory=True, memory_map=False, float_precision=None, storage_options=None, dtype_backend=<no_default>)
# Hier muss der Pfad angegeben werden, und alle anderen Parameter können direkt angesprochen werden
def read_csv(
    filepath_or_buffer,
    sep = ";",
    delimiter = ";",
    header = True):
	print()

# Hier werden jetzt nur die benötigten Parameter angegeben
read_csv("Beispielpfad", sep=",")
read_csv("Beispielpfad", header=False)
read_csv("Beispielpfad", sep=";", header=False)
read_csv("Beispielpfad", delimiter=";")

############################################

# Arbitrary Arguments
# Erlaubt, einen Parameter zu definieren, der beliebig viele Werte empfangen kann
def summe(*zahlen):
	x = 0
	for i in zahlen:  # zahlen ist hier ein Tupel
		x += i
	return x

summe(3, 4)
summe(6, 8, 9)
summe(6, 8, 9, 3, 1)
summe(1)
summe()

# Arbitrary Keyword Arguments
# Funktioniert wie Arbitrary Arguments, aber jeder Wert muss einen Namen haben
def printKurs(**tn):
	for k, v in tn.items():
		print(f"{k}: {v}")

printKurs(Trainer="Lukas", T1="Björn")  # Jeder Wert muss hier einen Schlüssel haben

############################################

# Unpacking
# Wird verwendet, um Listen an *Parameter weiterzugeben
# Gibt an den Parameter die INHALTE weiter, und nicht die Liste selbst
l = [1, 2, 3]
# summe(l)  # Funktioniert nicht

summe(*l)  # Zerlege die Liste in ihre Einzelteile und gib diese weiter (anstatt die gesamte Liste)