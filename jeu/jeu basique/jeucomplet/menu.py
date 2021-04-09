# -*- coding: utf-8 -*-
from tkinter import *
import random

def lancerhard():
    canvas.destroy()
    import Hard

def lancermedium():
    alea=randint(1,2)
    if alea == 1:
        canvas.destroy()
        import Hard
    else:
        canvas.destroy()
        import Easy

def lancereasy():
    canvas.destroy()
    import Easy

longueur,largeur=250,250

fenetre = Tk()
canvas = Canvas(fenetre, width=longueur, height=largeur, bg="yellow")
canvas.pack()
fenetre.title('Jeu de NIM sous python')
fenetre.resizable(False,False)

boutonquit = Button(canvas, text='Quitter', command = canvas.destroy)
boutonquit.place(x=100, y=225)

Facile = Button(canvas, text="Facile", command = lancereasy, height = 1, width = 5)
Facile.place(x=30, y=120)

Moyen = Button(canvas, text="Moyen", command = lancermedium, height = 1, width = 5)
Moyen.place(x=100, y=120)

Difficile = Button(canvas, text="Difficile", command = lancerhard, height = 1, width = 5)
Difficile.place(x=170, y=120)

Credits = Label(canvas, text="Made by : BH,LK", bg="Yellow")
Credits.place(x=85, y=200)

canvas.create_text(25, 0, anchor = NW, text="Jeu De NIM", font=("Impact",35))
canvas.create_text(29,40, anchor = NW, text="Classique", font=("Impact",35))



fenetre.mainloop()
