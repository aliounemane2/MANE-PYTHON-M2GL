#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmblaye
#
# Created:     02/06/2016
# Copyright:   (c) mmblaye 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class ClasseTesteUn:
    """
        DÃ©f class ClasseTesteUn
    """
    def __init__(self):
        self.attribut="Valeur Attribut"

class ClasseTesteDeux:
    """
        DÃ©f class ClasseTesteDeux
    """
    def __init__(self,attribut):
        self.attribut=attribut

class ClasseAttributClass:
    """
        DÃ©f class ClasseTesteDeux
    """
    nb=0
    def __init__(self):
        ClasseAttributClass.nb+=1
    def methodeDeClass(cls):
        """
            Les mÃ©thodes de classe prenne comme argument cls et non self
        """
        print(" NB = {}".format(cls.nb))
    """
        Il faut Expliciter que c'est une mÃ©thode de classe par l'instruction suivante
    """
    methodeDeClass=classmethod(methodeDeClass)

    def methodeStatic():
        print(" Static Methode ")

    """
        Il faut Expliciter que c'est une mÃ©thode static par l'instruction suivante
    """
    methodeStatic=staticmethod(methodeStatic)

c=ClasseTesteUn()
#print(c.attribut)
c.attribut="Changement"
#print(c.attribut)
d=ClasseTesteDeux("Passe Arg")
#print(d.attribut)
un=ClasseAttributClass()
#print(ClasseAttributClass.nb)
#print(un.nb)
deux=ClasseAttributClass()
#print(ClasseAttributClass.nb)
#print(deux.nb)
trois=ClasseAttributClass()
ClasseAttributClass.methodeDeClass()
ClasseAttributClass.methodeStatic()
