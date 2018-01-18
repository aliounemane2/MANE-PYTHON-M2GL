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

class ClasseIntrospection:
    """
        DÃƒÆ’Ã‚Â©f class ClasseTesteUn
    """
    def __init__(self):
        self.attribut1="Valeur Attribut 1"
        self.attribut2="Valeur Attribut 2"
        self.attribut3="Valeur Attribut 3"

c=ClasseIntrospection()
"""
    methode permettant d'explorer le contenu (visible ou caché d'un objet)
    dir :
        Elle prend en paramÃƒÂ¨tre un objet et renvoie la liste de ses attributs et mÃƒÂ©thodes.
"""
a=dir(c)
print(a)
print(c.__dict__)
c.__dict__["attribut2"]="Modif val Att 2"
print(c.__dict__)