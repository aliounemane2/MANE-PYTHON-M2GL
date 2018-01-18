#-*- coding: utf-8 -*-
import os

def nombre():

    # tab = [100, 200, 500, 50, 10, 25, 10, 55, 10]
    #
    nbre = int(input(" DONNEZ LE NOMBRE A  INSERER  "))
    compteur=0

    resultat = nbre

    while resultat>=500:
        resultat=nbre//500
        compteur = compteur+1
    print(resultat," billets de 500 ")
    # resultat = resultat - (compteur*500)



    compteur=0
    while resultat>=100:
        resultat=nbre//100
        compteur = compteur+1
        print(resultat," billets de 100 ")
    #resultat = nbre - (resultat*compteur)

    compteur=0

    while resultat>=50:
        resultat=nbre//50
        compteur = compteur+1
        print(resultat," billets de 50 ")
    # resultat = nbre - (resultat*compteur)

    compteur=0
    while resultat>=10:
        resultat=nbre//10
        compteur = compteur+1
        print(resultat, " billets de 10 ")
    resultat = nbre - (resultat*compteur)



def liste_monotone():
    tab = [10, 15, 50, 60, 40]
    if tab.sort() is not None:
        print(' La liste est Monotone')
    else:
        print(' La liste n est pas Monotone')






rep = "a"

while rep != "Q" and rep != "q":
    print(" APPUYER SUR -->> ")
    print(" A -->  AJOUT DE NOMBRE  ")
    print(" B -->  LISTE MONOTONE ")
    print(" Q -->  POUR QUITTER ")
    rep = input(" APPUYER -->> ")
    if rep == "A":
        nombre()
    if rep == "B":
        liste_monotone()




os.system("Pause")





