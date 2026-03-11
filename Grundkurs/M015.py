# GUI
# from tkinter import Tk, Label, Button
from tkinter import *

window = Tk()  # Fenster erzeugen
window.config(bg="#00FF00")
window.geometry("500x250+2500+300")
window.title("Mein erstes Fenster")

# Label erzeugen + platzieren
label = Label(text="Hallo Welt", name="output")
label.place(x=10, y=10, width=100, height=30)

# Button erzeugen + platzieren
button = Button(text="Klick mich!")
button.place(x=10, y=50, width=100, height=30)

i = IntVar(value=0)
def buttonClicked():
	current = i.get()
	current += 1
	w = window.nametowidget("output")
	w.config(text=current)
	i.set(current)

button.config(command=lambda: buttonClicked())  # command: Bei Button Klick, wird diese Methode ausgeführt

if __name__ == "__main__":
	window.mainloop()  # Fenster starten und laufen lassen