#-*- coding: utf-8 -*-
import os

#ALIOUNE MANE
# A L'ISI EN MASTER GENIE LOGICIELLE

def ajoutpers():

    nom = input(" DONNEZ LE NOM : ")
    pers = nom+"-"+";"
    f = open("fichier.txt", "a")
    f.write(pers)
    f.close()


#AFFICHAGE
def affichage():
    f = open("fichier.txt", "r")
    c = f.readlines()
    num = 1
    for l in c:
        tab = l.split(";")
        for i in tab:
            print(i)
    f.close()


def recherche(nom):
    f = open("fichier.txt", "r")
    c = f.readlines()
    p = "vide"
    for l in c:
        tab = l.split(";")
        for i in tab:
            tab2 = i.split("-")
            for k in tab2:
                if nom == k:
                    p = i
    return p


def supprimer(nom):

    f = open("fichier.txt", "r")
    c = f.readlines()
    p = []
    for l in c:
        tab = l.split(";")
        for i in tab:
            tab2 = i.split("-")
            for k in tab2:
                if nom == k:
                    i = "0"

            # if i != "0":
            #     p.append(i, "-")
            #     p.append(";")

    f.close()
    f = open("fichier.txt", "w")
    for id in p:
        f.write(id)
    f.close()
    affichage()



rep = "a"

while rep != "Q" and rep != "q":
    print(" APPUYER SUR -->> ")
    print(" A -->  POUR AJOUTER ")
    print(" F -->  POUR AFFICHER ")
    print(" R -->  POUR RECHERCHER ")
    print(" S -->  POUR SUPPRIMER ")
    print(" Q -->  POUR QUITTER ")
    rep = input(" APPUYER -->> ")
    if rep == "A":
        ajoutpers()
    if rep == "R":
        nom = input(" DONNEZ LE NOM A RECHERCHER ")
        print(recherche(nom))
    if rep == "F":
        affichage()
    if rep == "S":
        nom = input(" DONNEZ LE NOM A RECHERCHER ")
        supprimer(nom)



os.system("Pause")