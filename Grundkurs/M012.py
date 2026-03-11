# Fehlerbehandlung

# Oftmals können Fehler mit if-Bedingung behandelt werden
# Manchmal können Fehler nicht so einfach vorhergesehen werden -> try + except

# Beispiel
eingabe = "1" # input("Gib eine Zahl ein: ")
if eingabe.isnumeric():  # Option 1
	zahl = int(eingabe)
	print(zahl * 2)

try:  # Option 2
	zahl = int(eingabe)
	print(zahl * 2)
except ValueError:
	pass

# Wann try-except verwenden?
# Wenn der/die Fehler nicht vorhergesehen werden können
# z.B. Verbindungsaufbau zu Datenbank (kann fehlschlagen, kann im Skript nicht vorhergesehen werden)

###############################################################

# try-except im vollen Umfang
try:  # Im try-Block gibt es nicht viel Alternation
	zahl = int(eingabe)
	print(zahl * 2)
except ValueError:  # except + ein Fehler
	print("Eingabe ist keine Zahl")
except TypeError as e:  # except + ein Fehler mit Name (erlaubt Zugriff auf den Fehler)
	print(e)
except:  # except alleine: Alle (anderen) Fehler
	print("Anderer Fehler")  # Wird nur ausgeführt, wenn keine anderen except-Blöcke ausgeführt werden
	raise  # Lässt das Programm trotzdem abstürzen
else:  # Wird nur ausgeführt, wenn keine except-Blöcke ausgeführt wurden
	print("Keine Fehler")
finally:  # Wird immer ausgeführt, egal ob ein Fehler passiert ist oder nicht, aber auch wenn das Programm trotz des Blocks abstürzt
	print("Immer ausgeführt")  # Wird auch ausgeführt, wenn in einem except-Block der Absturz trotzdem passiert (raise)

# Warum try-except?
# Bei Entwicklung von Code für andere Entwickler, können wir nie wissen, wie die Anwendung/Fehlerbehandlung aussehen muss
# Mithilfe von raise können Fehler verursacht werden (Abstürze); diese können mit try-except pro User unabhängig verarbeitet werden
# Beispiele: print schreibt nur in die Konsole, anderer Entwickler haben u.a. eine GUI (Webseite, Desktopanwendung)
# In der GUI ist print(...) nicht sichtbar

# raise
# Lässt das Programm abstürzen
# Der andere Entwickler muss in weiterer Folge try-except für die Fehlerbehandlung benutzen
import time
jetzt = time.time()
if jetzt % 2 < 1:
	raise TimeoutError("Fehler in M012.py")

# Fehlermeldungen loggen
# Mithilfe von dem Traceback Modul

import Logger
try:
	print(2 / 0)
except ZeroDivisionError as e:
	# import traceback
	from traceback import format_exception
	with open("Log.txt", "w") as log:
		for zeile in format_exception(e):
			log.write(zeile)

	Logger.logException(e)  # Code in einem anderen Skript ablegen

# Debugging