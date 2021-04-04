# -*- coding: utf-8 -*-
from random import *
import time


allumettes=randint(5, 12)




joueur=randint(0,1)
if joueur == 0:
    print("C'est vous qui commencez à jouer")
    print ("Il y a ",allumettes," allumettes")
    while allumettes!=0 or allumettes>0:
        print("Tour du joueur")
        retirer=int(input("Veuillez rentrer un chiffre de 1 à 3: "))
        while retirer <=0 or retirer >=4:
            retirer=int(input("Erreur, Veuillez rentrer un chiffre de 1 à 3: "))
        allumettes -= retirer
        print ("il reste",allumettes ,"allumettes")
        if allumettes <= 0:
            print("Vous avez gagné")
            break
        print("Tour du bot")
        if (allumettes-1)%4==0:
            allumettes-=1
        elif (allumettes-2)%4==0:
            allumettes-=2
        elif (allumettes-3)%4==0:
            allumettes-=3
        else:
            allumettes-=randint(1,3)
        print ("il reste",allumettes ,"allumettes")
        if allumettes<=0:
            print ("vous avez perdu")
            print("Le jeu est terminé, merci d'avoir essayé mais notre bot est PARFAIT *s'étouffe*")
            break

else:
    print("c'est l'ordinateur qui va commencer")
    print ("Il y a ",allumettes," allumettes")
    while allumettes!=0 or allumettes>0:
        print("Tour du bot")
        if (allumettes-1)%4==0:
            allumettes-=1
        elif (allumettes-2)%4==0:
            allumettes-=2
        elif (allumettes-3)%4==0:
            allumettes-=3
        else:
            allumettes-=randint(1,3)
        print ("il reste",allumettes ,"allumettes")
        if allumettes<=0:
            print ("vous avez perdu")
            print("Le jeu est terminé, merci d'avoir essayé mais notre bot est PARFAIT *s'étouffe*")
            break
        print("Tour du joueur")
        retirer=int(input("Veuillez rentrer un chiffre de 1 à 3: "))
        while retirer <=0 or retirer >=4:
            retirer=int(input("Erreur, Veuillez rentrer un chiffre de 1 à 3: "))
        allumettes -= retirer
        print ("il reste",allumettes ,"allumettes")
        if allumettes <= 0:
            print("Vous avez gagné")
            time.sleep(5)
            print("Ouais bon en fait tu as de la chance le bot a pop dans le noyau va jouer au loto")
            break
        