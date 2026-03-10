# Decorator
# Code zu einer Funktion hinzufügen, ohne die Funktion selbst zu ändern
# Wird mit @<Name> an eine beliebige Funktion angehängt

# func: Die dekorierte Funktion (hier halloWelt())
def testDecorator(func):
	def wrapper():
		print("Vor der Funktion")
		func()  # Hier kann vor/nach der dekorierten Funktion beliebiger Python Code ausgeführt werden
		print("Nach der Funktion")
	return wrapper

@testDecorator  # Über @<Name> wird die nächste Funktion dekoriert (die halloWelt Funktion)
def halloWelt():
	print("Hallo Welt")

halloWelt()  # Dieser Aufruf erzeugt hier 3 Ausgaben

##########################################################

# Beispiel: Zeitmesser
def generateList(length):
	x = list(range(length))

# import time
# start = time.time()
# generateList(100_000_000)
# end = time.time()
# print(end - start)  # Dieser Code kann auch per Decorator aktiviert werden

def measureTime(func):  # *args wird hier benötigt, damit Decorator eine Funktion akzeptiert, die Parameter erfordert
	def wrapper(*args, **kwargs):  # **kwargs sollte hier immer hinzugefügt werden, weil es kostenlos ist
		import time
		start = time.time()
		func(*args, **kwargs)  # Hier bei func muss *args und **kwargs mitgegeben werden
		end = time.time()
		print(func.__name__)
		print(f"{round(end - start, 3)}s")
	return wrapper

@measureTime
def generateList(length):
	x = list(range(length))

generateList(100_000_000)
generateList(10_000_000)

##########################################################

# @property
# Erlaubt, vor dem Lesen/Schreiben eines Feldes innerhalb einer Klasse das Ausführen von Code
# Stichwort: Sicherheit

class Fahrzeug:
	def __init__(self):
		self.aktV = 0

	@property
	def aktV(self):
		return self.aktV

	@aktV.setter
	def aktV(self, value):  # Hier kann das = mit einem Stück Code versehen werden
		if value >= 0 and value <= 200:
			self._aktV = value

	@aktV.getter
	def aktV(self):
		return self._aktV

	# def setAktV(self, a):
	# 	if a >= 0 and a <= 200:
	# 		self._aktV = a

fzg = Fahrzeug()
fzg.aktV = 123  # setter-Methode wird ausgeführt
print(fzg.aktV)  # getter-Methode wird ausgeführt

# fzg.aktV.setAktV(123)