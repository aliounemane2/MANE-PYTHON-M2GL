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

class ClasseProprietes:
    """
        Les propriÃ©tÃ©s sont un moyen transparent de manipuler des attributs d'objet.
        Elles permettent de dire Ã  Python :
            Quand un utilisateur souhaite modifer cet attribut,fais cela
    """
    def __init__(self):
        self.attribut1="Valeur Attribut 1"
        self.attribut2="Valeur Attribut 2"
        self._att_propriete="Valeur Attribut Propriété"

    # le _ est mis par convention
    def _get_att_propriete(self):
        print(" Récuération att_propriete")
        return self._att_propriete

    def _set_att_propriete(self,new_att_propriete):
        print(" Modification _att_propriete")
        rep=input("Voulez vous modifier l'attribt")
        if(rep=='o'):
            self._att_propriete=new_att_propriete

    # Définition de la propriété : propriete(methode_accesseur, methode_mutateur, methode_suppression,methode_aide).
    att_propriete=property(_get_att_propriete,_set_att_propriete)

c=ClasseProprietes()
#print(c.attribut1)
#print(c.att_propriete)
c.att_propriete="Novelle Att Propriété"
print(c.att_propriete)