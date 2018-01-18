# -*-coding:utf-8 -*
class Personne:

    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age

    def afficher(self):
        print(self.prenom ," ",self.nom, " à ",self.age," ans ")

    def __del__(self):
        """ Mé thode appel ée quand l'objet est supprim é"""
        print ("Suppression de l'objet ")

    def __repr__(self):
        """ __repr__ est une méthode de représentation
        - Elle permet de personnaliser l'ecriture de l'objet
        - utiliser un return et non un print
        """
        ret="Représentation de "+str(self.prenom) +" "+str(self.nom)+" qui à "+str(self.age)+" ans "
        return ret

    def __str__(self):
        """ __str__ est une méthode de représentation
        - Elle permet de caster l'ecriture de l'objet
        - Elle gére que le STR (REPR et plus forte
        - utiliser un return et non un print
        """
        ret="Représentation de "+str(self.prenom) +" "+str(self.nom)+" qui à "+str(self.age)+" ans "
        return ret

    def __getattr__(self,att):
        """ __getattr__ est une méthode de représentation
        - Elle permet de personnaliser le message lorsque l'attribut
        n'existe pas
        """
        print("l'attribut ",att,"  n'existe pas")

    def __setattr__ (self , nom_attr , val_attr ):
         """ Méthode appelée quand on fait objet.nom_attr = val_attr .
             On se charge d'enregistrer l'objet """
         object. __setattr__ (self , nom_attr , val_attr )
         self . enregistrer ()

    def __delattr__(self,att):
        """ __delattr__ est une méthode de représentation
        - Elle permet d'annuler la suppréssion d'un attribut
        - si elle est définie l'attibut ne sera pas supprimer
        """
        print("Vous tentez de supprimer l'attribut ",att)

p1=Personne("Fall","Doudou",15)
print(p1)
#del(p1)
