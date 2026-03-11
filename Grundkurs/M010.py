# Klassen und Objekte

# Klasse
# Komplexe Datentypen darstellen
# Werden mit Variablen und Funktionen befüllt

# Datentypen Quiz
# - int: Ganze Zahl
# - float: Kommazahl
# - str: Zeichenfolge
# - list: Aufzählung von Daten
# - Person: ?

# Für Person müssen wir eine eigene Klasse definieren (weil Person komplex ist)

# 2 Typen von Klassen
# - Funktionsklassen
# - Datenklassen

# Person
# Datenpunkte:
# - Vorname
# - Nachname
# - Geschlecht
# - Adresse
# - Geburtsdatum
# - ...

# Klassendefinition
class Person:
	"""
	docstring

	Dokumentationskommentar

	Beschreibt eine Funktion/Klasse (mit Maus über Typname wird die Doku aufgerufen)

	Muss unter der Definition verwendet werden
	"""
	def __init__(self, v: str, n: str, g: str, a: int):
		"""
		__init__

		Wird immer ausgeführt, wenn das Objekt erstellt wird (-> der Startcode von jedem Objekt)

		Hier werden die konkreten Werte empfangen, und angegeben, welche werden allg. empfangen werden sollen
		"""

		self.vorname = v  # Attribut auf den Objekten registrieren
		self.nachname = n
		self.geschlecht = g
		self.alter = a

#####################################################

# Objekte
# Konkrete Instanzen von dem Bauplan
# Hier werden die verschiedenen Objekte erzeugt, und anhand ihre Inhalte unterschieden voneinander
person1 = Person("Lukas", "", "M", 27)  # Hier werden konkrete Objekte erstellt, diese benötigen konkrete Daten
person2 = Person(v="Björn", n="", g="M", a=51)  # Hier muss ein Parameter gegeben werden (v), dieser wird in ein Attribut namens "vorname" hineingeschrieben

print(person1.vorname)
print(person2.vorname)

#####################################################

# Person verbessern
# - Parameter optional machen
# - Funktion hinzufügen
# - __str__ überschreiben
class PersonCool:
	def __init__(self, v: str, n: str, g: str = None, a: int = None):
		# None = Null (nichts)
		self.vorname = v
		self.nachname = n
		self.geschlecht = g
		self.alter = a

	def __str__(self):
		"""
		__str__

		Gibt eine Stringrepräsentation von dem Objekt zurück

		Normalerweise: <__main__.Typname at 0x0000000000000000000123456789> (Typname + Speicheradresse)

		Hier kann die Stringausgabe angepasst werden
		"""
		return f"Vorname: {self.vorname}, Nachname: {self.nachname}"

	def __add__(self, other):
		"""
		Die __ Methoden (Special Methods)

		Überschreibbare Methoden, um konkretes Verhalten zu implementieren

		z.B.: Addieren von 2 Personen Objekten aufeinander (macht wenig Sinn)
		"""
		pass  # pass: Leere Operation; wird für Aufbauten ohne konkreten Code verwendet (Platzhalter)

	# Funktionen eher selten in Datenklassen
	def sprechen(self, text: str):
		print(f"{self.vorname} sagt: {text}")


p3 = PersonCool("Max", "Mustermann")
print(p3)

p3.sprechen("Hallo")