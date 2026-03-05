# Module
# Andere Python Skripte verbinden (und Inhalt aus diesen Skripten benutzen)

# import
# Lädt alle Member (Variablen, Funktionen, Klassen) aus einem anderen Skript, und macht diese hier verwendbar
# Syntax: import <Name> (as <Alias>)
import M007
M007.hallo("M008")

# WICHTIG: Beim import wird das gesamte andere Skript ausgeführt
# D.h. das andere Skript sollte niemals Code enthalten, der Outputs erzeugt
import M007 as M
M.hallo("8")
# M007.summe(1, 2, 3)  # nicht mehr möglich

# from import
# Lädt konkrete Member aus einem Skript, und bindet diese direkt hier ein
# D.h., die Member können ohne den Prefix (Name des anderen Skriptes) verwendet werden
# Syntax: from <Name> import <Member1>, <Member2>, ...
from M007 import hallo, summe
# from M007 import *  # Importiert alle Member aus dem anderen Skript
hallo("M008")

# WICHTIG: Beim import wird das gesamte andere Skript ausgeführt
# D.h. das andere Skript sollte niemals Code enthalten, der Outputs erzeugt

########################################################

# Modul Suchpfade
import sys
for p in sys.path:
	print(p)

# Eigene Pfade hinzufügen
sys.path.append("C:\\Users\\lk3\\Desktop")

import xyz  # Skript von Desktop

########################################################

# Externe Pakete installieren

# 2 Optionen:
# - Python Packages
# - pip (Terminal)
import numpy
print(numpy.pi)

# pip (Terminal)
import pandas

########################################################

# Main Methode
# Stück Code, welches bei direktem Start (nicht bei Import) ausgeführt wird
# Wird in vielen Skripten verwendet
if __name__ == "__main__":
	print("...")  # Hier wird beliebiger Code hineingelegt, der nur bei direkter Ausführung passieren soll (z.B. Tests)

# __name__
# Globale Variable, welche entweder __main__ (bei direkter Ausführung) oder den Namen des Skriptes selbst enthält (bei Import)
print(__name__)  # __main__

########################################################

# Packages
# = Ordner
# Beim Import muss der Ordnername mit angegeben werden
import M008b.Test as t
t.printHallo()

# __init__.py
# Python Skript, welches bei einem Import auf der Ordner ausgeführt wird
# Bei einem Skript, bei mehreren Skripten oder beim gesamten Ordner