# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox
from random import *
from time import *

#canvas.after(temps(en ms),fonction)

allumettes = []
for i in range(5):
    allumettes.append(randint(1, 7))

def remplissage(str): #pour que tous les binaires aient 3 chiffres (on rajoute des 0)
    liste=[]
    for x in str:
        liste.append(x)
    while len(liste)<5:
        liste.insert(2,'0')
    str=''
    for x in liste:
        str+=x
    return str

def remplacement(str,place,content): #pour remplacer un élément dans un str (l'élement à l'emplacement "place" dans "str" devient "content")
    liste=[]
    for x in str:
        liste.append(x)
    liste.pop(place)
    liste.insert(place,content)
    str=''
    for x in liste:
        str+=x
    return str

def bot():
    binaire=remplissage(bin(0)) #binaire sera le résultat de "l'addition" des 5 paquets d'allumettes, sur lequel le bot se basera pour trouver le noyau
    for x in range(5):
        x=remplissage(bin(allumettes[x]))
        for y in range(2,5):
            remplacer=str((int(binaire[y])+int(x[y]))%2) # 0+0 = 0 ; 0+1/1+0 = 1 ; 1+1 = 0
            binaire=remplacement(binaire,y,remplacer)

    verif=0 #le bot cherche s'il ne reste plus qu'un paquet non-vide
    for i in range(5):
        if allumettes[i]>0:
            verif+=1
            packet=i
    if verif==1:
        retirer=allumettes[packet]
    else:
        if binaire=="0b000": #Si on est déjà dans le noyau
            packet=randint(0,4)
            while allumettes[packet]==0:
                packet=randint(0,4)
            retirer=randint(1,allumettes[packet])
        elif binaire=="0b001":
            for i in range(4):
                if allumettes[i]%2==1:
                    packet=i
            retirer=1
        elif binaire=="0b010":
            for i in range(4):
                if allumettes[i]>=2 and allumettes[i]!=4 and allumettes[i]!=5:
                    packet=i
            retirer=2
        elif binaire=="0b011":
            for i in range(4):
                if allumettes[i] in [2,6]:
                    packet=i
                    retirer=1
                elif allumettes[i] in [3,7]:
                    packet=i
                    retirer=3
        elif binaire=="0b100":
            for i in range(4):
                if allumettes[i]>=4:
                    packet=i
            retirer=4
        elif binaire=="0b101":
            for i in range(4):
                if allumettes[i]>=5:
                    packet=i
                    retirer=5
                elif allumettes[i]==4:
                    packet=i
                    retirer=3
        elif binaire=="0b110":
            for i in range(4):
                if allumettes[i]>=6:
                    packet=i
                    retirer=6
                elif allumettes[i]>=4:
                    packet=i
                    retirer=2
        else: #binaire=="0b111"
            for i in range(4):
                if allumettes[i]==7:
                    packet=i
                    retirer=7
                elif allumettes[i]==6:
                    packet=i
                    retirer=5
                elif allumettes[i]==5:
                    packet=i
                    retirer=3
                elif allumettes[i]==4:
                    packet=i
                    retirer=1
  
    indic="le bot a retiré "+str(retirer)+" allumettes dans le paquet "+str(packet)
    labelindic.config(text=indic)
    allumettes[packet]-=retirer
    allus1.config(text=allumettes[0])
    allus2.config(text=allumettes[1])
    allus3.config(text=allumettes[2])
    allus4.config(text=allumettes[3])
    allus5.config(text=allumettes[4])
    if allumettes==[0,0,0,0,0]:
        print ("vous avez perdu")
        print("Le jeu est terminé, merci d'avoir essayé mais notre bot est PARFAIT *s'étouffe*")


def valider1():
    retirer=allu1.get()
    if retirer<=0:
        labelindic.config(text="vous n'avez pas rentrer de nombre valide")
    else:
        packet=0
        indic="vous avez retiré "+str(retirer)+" allumettes dans le paquet 1"
        labelindic.config(text=indic)
        allu1.set(0)
        if allumettes[packet]>=retirer:
            allumettes[packet] -= retirer
        else: #si on retire plus d'allumattes qu'il y en a dans le paquet, ça revient à en retirer autant
            allumettes[packet]=0
        allus1.config(text=allumettes[0])
        canvas.after(1000,bot)

def valider2():
    retirer=allu2.get()
    if retirer<=0:
        labelindic.config(text="vous n'avez pas rentrer de nombre valide")
    else:
        packet=1
        indic="vous avez retiré "+str(retirer)+" allumettes dans le paquet 2"
        labelindic.config(text=indic)
        allu2.set(0)
        if allumettes[packet]>=retirer:
            allumettes[packet] -= retirer
        else:
            allumettes[packet]=0
        allus2.config(text=allumettes[1])
        canvas.after(1000,bot)

def valider3():
    retirer=allu3.get()
    if retirer<=0:
        labelindic.config(text="vous n'avez pas rentrer de nombre valide")
    else:
        packet=2
        indic="vous avez retiré "+str(retirer)+" allumettes dans le paquet 3"
        labelindic.config(text=indic)
        allu3.set(0)
        if allumettes[packet]>=retirer:
            allumettes[packet] -= retirer
        else:
            allumettes[packet]=0
        allus3.config(text=allumettes[2])
        canvas.after(1000,bot)

def valider4():
    retirer=allu4.get()
    if retirer<=0:
        labelindic.config(text="vous n'avez pas rentrer de nombre valide")
    else:
        packet=3
        indic="vous avez retiré "+str(retirer)+" allumettes dans le paquet 4"
        labelindic.config(text=indic)
        allu4.set(0)
        if allumettes[packet]>=retirer:
            allumettes[packet] -= retirer
        else:
            allumettes[packet]=0
        allus4.config(text=allumettes[3])
        canvas.after(1000,bot)

def valider5():
    retirer=allu5.get()
    if retirer<=0:
        labelindic.config(text="vous n'avez pas rentrer de nombre valide")
    else:
        packet=4
        indic="vous avez retiré "+str(retirer)+" allumettes dans le paquet 5"
        labelindic.config(text=indic)
        allu5.set(0)
        if allumettes[packet]>=retirer:
            allumettes[packet] -= retirer
        else:
            allumettes[packet]=0
        allus5.config(text=allumettes[4])
        canvas.after(1000,bot)

fenetre=Tk()
canvas = Canvas(fenetre, width=800, height=600, bg="green")
canvas.pack()
fenetre.title('Difficile')
fenetre.resizable(False,False)

jeunim = Label(canvas, text="JEU DE NIM", font=("Impact",40), bg="green")
jeunim.place(x=290, y=2)

labelindic= Label(canvas, text="Entrer le nombre d'allumettes que vous voulez enlever en dessous du paquet voulu", font=("Arial",12), bg="green")
labelindic.place(x=120, y=100)

paquet1= Label(canvas, text="Dans le paquet 1,\n il y en a:", font=("Arial",12), bg="green")
paquet1.place(x=20, y=200)
paquet2= Label(canvas, text="Dans le paquet 2,\n il y en a:", font=("Arial",12), bg="green")
paquet2.place(x=180, y=200)
paquet3= Label(canvas, text="Dans le paquet 3,\n il y en a:", font=("Arial",12), bg="green")
paquet3.place(x=340, y=200)
paquet4= Label(canvas, text="Dans le paquet 4,\n il y en a:", font=("Arial",12), bg="green")
paquet4.place(x=500, y=200)
paquet5= Label(canvas, text="Dans le paquet 5,\n il y en a:", font=("Arial",12), bg="green")
paquet5.place(x=660, y=200)

allus1 = Label(canvas, text=str(allumettes[0]), font=("Arial",35), bg="green")
allus1.place(x=70, y=250)
allus2 = Label(canvas, text=str(allumettes[1]), font=("Arial",35), bg="green")
allus2.place(x=230, y=250)
allus3 = Label(canvas, text=str(allumettes[2]), font=("Arial",35), bg="green")
allus3.place(x=390, y=250)
allus4 = Label(canvas, text=str(allumettes[3]), font=("Arial",35), bg="green")
allus4.place(x=550, y=250)
allus5 = Label(canvas, text=str(allumettes[4]), font=("Arial",35), bg="green")
allus5.place(x=710, y=250)

allu1=IntVar()
Entry1= Entry(canvas, textvariable=allu1)
Entry1.place(x=20, y=320)
allu2=IntVar()
Entry2= Entry(canvas, textvariable=allu2)
Entry2.place(x=180, y=320)
allu3=IntVar()
Entry3= Entry(canvas, textvariable=allu3)
Entry3.place(x=340, y=320)
allu4=IntVar()
Entry4= Entry(canvas, textvariable=allu4)
Entry4.place(x=500, y=320)
allu5=IntVar()
Entry5= Entry(canvas, textvariable=allu5)
Entry5.place(x=660, y=320)

Bouton1= Button(canvas, text='OK', command=valider1)
Bouton1.place(x=50,y=350)
Bouton2= Button(canvas, text='OK', command=valider2)
Bouton2.place(x=210,y=350)
Bouton3= Button(canvas, text='OK', command=valider3)
Bouton3.place(x=370,y=350)
Bouton4= Button(canvas, text='OK', command=valider4)
Bouton4.place(x=530,y=350)
Bouton5= Button(canvas, text='OK', command=valider5)
Bouton5.place(x=690,y=350)

fenetre.mainloop()
