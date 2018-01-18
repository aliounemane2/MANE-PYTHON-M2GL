# -*-coding:utf-8 -*
import os

#PROJET FAIT PAR ALIOUNE MANE
# A L'ISI EN MASTER GENIE LOGICIELLE


# AJOUT 
def ajoutpers():

    nom = input(" DONNEZ LE NOM ET LE PRENOM ")
    profession = input(" DONNEZ LA PROFESSION ")
    tel = input(" DONNEZ LE TELEPHONE ")
    pers = nom+"-"+profession+"-"+tel+";"
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
# RECHERCHE


def recherche(tel):
    f = open("fichier.txt", "r")
    c = f.readlines()
    p = "vide"
    for l in c:
        tab = l.split(";")
        for i in tab:
            tab2 = i.split("-")
            for k in tab2:
                if tel == k:
                    p = i
    return p


#SUPPRIMER

def supprimer(tel):

    f = open("fichier.txt", "r")
    c = f.readlines()
    p = []
    for l in c:
        tab = l.split(";")
        for i in tab:
            tab2 = i.split("-")
            for k in tab2:
                if tel == k:
                    i = "0"
            if i != "0":
                p.append(i, "-")
                p.append(";")
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
        tel = input(" DONNEZ LE TELEPHONE A RECHERCHER ")
        print(recherche(tel))
    if rep == "F":
        affichage()
    if rep == "S":
        tel = input(" DONNEZ LE TELEPHONE A RECHERCHER ")
        supprimer(tel)

    

os.system("Pause")