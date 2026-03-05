# Input/Output

# input
# Wartet auf eine Usereingabe
# Diese Usereingabe wird bei Enter in einer Variable gespeichert
b = False
if b:
	eingabe = input("Gib deinen Namen ein: ")
	print(f"Hallo {eingabe}")

#######################################################

# open
# Datei öffnen
# Muss einen Modus enthalten (read oder write)
file = open("Output.txt", "w")
file.write("Hallo von M009!")
file.write("Zeile 2")

# Wenn wir fertig sind mit dem File, muss es geschlossen
file.flush()  # flush: Schreibt den Buffer (im Arbeitsspeicher) in den File nieder
file.close()  # close: Schließt den Stream zu dem File (damit es von anderen Programmen weiterverwendet werden kann)

# Datei lesen
fileR = open("Output.txt", "r")
lines = fileR.readlines()  # Liest das gesamte File; gibt eine String-Liste zurück (Zeile für Zeile)
fileR.close()

print(lines)

#######################################################

# Escape-Sequenzen
# Undruckbare Zeichen in einen String einbetten
# \n: Zeilenumbruch (\r als Alternative)
# \t: Tabulator
# \\: Backslash (nachdem ein einzelner Backslash eine Escape-Sequenz wäre)
# https://learn.microsoft.com/de-de/cpp/c-language/escape-sequences?view=msvc-170

file3 = open("Output.txt", "w")
file3.write("Hallo\n")
file3.write("Welt\n")
file3.close()  # Impliziert automatisch flush()

#######################################################

# with-Statement
# Schließt automatisch das File am Ende des Blocks
# Sollte immer verwendet werden (funktioniert auch bei anderen externen Schnittstellen, z.B. DB, API, ...)
with open("Output.txt", "w") as file4:
	file4.write("Hallo Welt")

#######################################################

# rstring
# Raw String
# String, der keine Escape-Sequenzen interpretiert
# Wird primär für Pfade verwendet
pfad = "C:\\Users\\lk3\\source\\repos\\Python_Grundkurs_2026_03_02\\.venv\\Scripts\\python.exe"
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2026_03_02\.venv\Scripts\python.exe"
pfadRF = rf"C:\Users\lk3\source\repos\Python_Grundkurs_2026_03_02\.venv\Scripts\{file}"

#######################################################

# Andere Pfadoperationen
import os.path

if os.path.exists("Output.txt"):
	print("Output.txt existiert bereits")

# Pfade Betriebssystemunabhängig zusammenbauen
print(os.path.join("Pfad1", "Pfad2", "Pfad3"))