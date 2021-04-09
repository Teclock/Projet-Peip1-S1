# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox
from random import *

fenetre=Tk()
canvas = Canvas(fenetre, width=800, height=600, bg="yellow")
canvas.pack()
fenetre.title('Difficile')
fenetre.resizable(False,False)

allumettes=randint(5,12)

allus = Label(canvas, anchor = CENTER, text=str(allumettes), font=("Arial",35))
allus.place(x=390, y=250)

def retirer1():
    global allumettes
    allumettes=str(int(allumettes)-1)
    allus.config(text=str(allumettes))
    allumettes=int(allumettes)
    if allumettes <= 0:
        tkinter.messagebox.showinfo("Gagné", "Félicitations!")
        canvas.destroy()
    allumettes-=randint(1,3)
    allus.config(text=str(allumettes))
    allumettes=int(allumettes)
    if allumettes<=0:
        tkinter.messagebox.showinfo("Perdu", "Félicitations! Tu as perdu!")



def retirer2():
    global allumettes
    allumettes=str(int(allumettes)-2)
    allus.config(text=str(allumettes))
    allumettes=int(allumettes)
    if allumettes <= 0:
        tkinter.messagebox.showinfo("Gagné", "Gagné")
        canvas.destroy()
    if (allumettes-1)%4==0:
        allumettes-=1
        allus.config(text=str(allumettes))
        allumettes=int(allumettes)
    elif (allumettes-2)%4==0:
        allumettes-=2
        allus.config(text=str(allumettes))
        allumettes=int(allumettes)
    elif (allumettes-3)%4==0:
        allumettes-=3
        allus.config(text=str(allumettes))
        allumettes=int(allumettes)
    else:
        allumettes-=randint(1,3)
        allus.config(text=str(allumettes))
        allumettes=int(allumettes)
    if allumettes<=0:
        tkinter.messagebox.showinfo("Perdu", "Félicitations! Tu as perdu!")



def retirer3():
    global allumettes
    allumettes=str(int(allumettes)-3)
    allus.config(text=str(allumettes))
    allumettes=int(allumettes)
    if allumettes <= 0:
        tkinter.messagebox.showinfo("Gagné", "Gagné")
        canvas.destroy()
    if (allumettes-1)%4==0:
        allumettes-=1
        allus.config(text=str(allumettes))
        allumettes=int(allumettes)
    elif (allumettes-2)%4==0:
        allumettes-=2
        allus.config(text=str(allumettes))
        allumettes=int(allumettes)
    elif (allumettes-3)%4==0:
        allumettes-=3
        allus.config(text=str(allumettes))
        allumettes=int(allumettes)
    else:
        allumettes-=randint(1,3)
        allus.config(text=str(allumettes))
        allumettes=int(allumettes)
    if allumettes<=0:
        tkinter.messagebox.showinfo("Perdu", "Félicitations! Tu as perdu!")


joueur = Label(canvas, anchor = CENTER, text="Tour du joueur", font=("Arial",12))
joueur.place(x=50, y=100)


ilreste = Label(canvas, anchor = CENTER, text="Il reste", font=("Courier",24))
ilreste.place(x=333, y=200)

allumettess = Label(canvas, anchor = CENTER, text="allumettes", font=("Courier",24))
allumettess.place(x=320, y=320)

jeunim = Label(canvas, anchor = N, text="Jeu des allumettes", font=("Impact",32), bg="yellow")
jeunim.place(x=250, y=2)


retirer1 = Button(canvas, text='-1', command = retirer1)
retirer1.place(x=200, y=500)

retirer2 = Button(canvas, text='-2', command = retirer2)
retirer2.place(x=398, y=500)

retirer3 = Button(canvas, text='-3', command = retirer3)
retirer3.place(x=600, y=500)

fenetre.mainloop()
