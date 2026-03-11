# Vererbung
# Basisklassen definieren, welche ihre Inhalte (Attribute und Funktionen) an alle Unterklassen weitergeben

# Beispiel: Object
# In Python gibt es eine Klasse namens object
# Diese Klasse fungiert als Oberklasse von allen Klassen in Python
# Diese Klasse gibt alle Methoden weiter, die mit __ beginnen (__init__, __str__, ...)

# Realität: Tiere, Pflanzen, Autos, ...

# Beispiel: Lebewesen -> Mensch, Hund, Katze

class Lebewesen:
	def __init__(self, alter: int):
		self.alter = alter

	def bewegen(self, distanz: int):
		print(f"Das Lebewesen bewegt sich um {distanz}m.")

	# Standardimplementation
	# Kann in den Unterklassen angepasst werden; ist dies nicht der Fall, wird dieser Output erzeugt
	def __str__(self):
		if type(self) == Mensch:
			print("Es ist ein Mensch")
		elif type(self) == Katze:
			print("Es ist eine Katze")

		return f"Lebewesen Alter: {self.alter}"


# Vererbung herstellen über Klassenname in Klammer
class Mensch(Lebewesen):
	# Wenn der Mensch selbst __init__ implementieren soll, muss hier eine Verkettung stattfinden
	# -> super()
	def __init__(self, alter: int, vorname: str):
		super().__init__(alter)  # Führe den Code von Lebewesen aus (reicht alter nach oben weiter)
		self.vorname = vorname

	def __str__(self):
		x = super().__str__()
		return x + f", Vorname: {self.vorname}"

# Mensch und Katze sind nebeneinander (Vererbungshierarchie)
class Katze(Lebewesen):
	def __init__(self, alter: int, fellfarbe: str):
		super().__init__(alter)
		self.fellfarbe = fellfarbe

	def __str__(self):
		x = super().__str__()
		return x + f", Fellfarbe: {self.fellfarbe}"


# Mensch hat __init__ und bewegen vererbt bekommen (von Lebewesen)
m = Mensch(33, "Lukas")
m.bewegen(10)

print(m)

k = Katze(1, "Braun")
print(k)