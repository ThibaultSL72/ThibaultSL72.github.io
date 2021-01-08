from tkinter import *
import random

fenetre = Tk()

canvas = Canvas(fenetre, width=400, height=400)
canvas.pack()

def restart():
    canvas.delete("all")
    for x in range(0, random.randint(0,500)):
        color = '{:06x}'.format(random_color())
        x1 = random.randint(0,400)
        y1 = random.randint(0,400)
        x2 = random.randint(0,400)
        y2 = random.randint(0,400)
        ligne = canvas.create_polygon(x1, y1, x2, y2,\
            fill =('#'+ color), outline='#'+ color)

def random_color():
    return random.randint(0,0x1000000)

for x in range(0, random.randint(0,500)):

    color = '{:06x}'.format(random_color())
    x1 = random.randint(0,400)
    y1 = random.randint(0,400)
    x2 = random.randint(0,400)
    y2 = random.randint(0,400)
    ligne = canvas.create_polygon(x1, y1, x2, y2,\
        fill =('#'+ color), outline='#'+ color)

label = Label(fenetre, text="Hello, World")
label.pack()

Bouton_sortie = Button(fenetre, text="RageQuit", command=fenetre.quit)
Bouton_sortie.pack()

Bouton_restart = Button(fenetre, text="Restart", command=restart)
Bouton_restart.pack()

fenetre.mainloop()
