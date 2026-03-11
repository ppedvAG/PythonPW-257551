# List Comprehension
# Kurzschreibweise zur Erstellung von Listen
# Innerhalb der Listenklammern wird eine Schleife ablegt; diese erzeugt eine Liste aus den Ergebnissen

# Ohne LC
zahlen = []
for i in range(10):
	zahlen.append(i)
print(zahlen)

# LC
zahlenLC = [i for i in range(10)]  # Schleife schreiben, i an den Anfang setzen
print(zahlenLC)

######################################################

# If-Bedingung
zahlenDurch3Und5 = []
for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0:
		zahlenDurch3Und5.append(i)
print(zahlenDurch3Und5)

# LC
zahlenDurch3Und5LC = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(zahlenDurch3Und5LC)

emails = ["abc@def.de", "abcdef.de", "abc@def.de", "abcdef.de", "abc@def.de"]
emailsMitAt = [m for m in emails if "@" in m]  # Alle Emails mit @ finden
print(emailsMitAt)

######################################################

# Linke Seite verändern

# True/False je nach dem, ob gerade oder ungerade
evenOdd = []
for i in range(100):
	if i % 2 == 0:
		evenOdd.append(f"{i}, True")
	else:
		evenOdd.append(f"{i}, False")
print(evenOdd)

# LC
evenOddLC = [f"{i}, {i % 2 == 0}" for i in range(100)]
print(evenOddLC)

######################################################

# Verschachtelte Schleife
for m in range(60):
	for s in range(60):
		print(f"{m:02}:{s:02}")

# LC
stoppuhrLC = [f"{m:02}:{s:02}"
			  for m in range(60)
			  for s in range(60)]
print(stoppuhrLC)

######################################################

# Ternary Operator
# Linke Seite anhand einer Bedingung verändern
for x in range(1, 101):
	if x % 3 == 0 and x % 5 == 0:
		print("FizzBuzz")
	elif x % 3 == 0:
		print("Fizz")
	elif x % 5 == 0:
		print("Buzz")
	else:
		print(x)

# LC
fizzBuzzLC = ["FizzBuzz" if x % 3 == 0 and x % 5 == 0 else
			  "Fizz" if x % 3 == 0 else
			  "Buzz" if x % 5 == 0 else
			  x for x in range(1, 101)]
print(fizzBuzzLC)