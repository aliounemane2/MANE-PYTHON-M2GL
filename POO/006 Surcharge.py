class Vecteur:
    def __init__(self,abs=0,ord=0):
        self.abs=abs
        self.ord=ord

    def __repr__(self):
        return " point : ({},{})".format(self.abs,self.ord)

    def __add__(self,v1):
        new_point=Vecteur()
        new_point.abs=self.abs
        new_point.ord=self.ord
        new_point.abs+=v1.abs
        new_point.ord+=v1.ord
        return new_point

"""
__sub__      : surcharge de l'opérateur - ;
__mul__      : surcharge de l'opérateur * ;
__truediv__  : surcharge de l'opérateur / ;
__floordiv__ : surcharge de l'opérateur // (division entière) ;
__mod__      : surcharge de l'opérateur % (modulo) ;
__pow__      : surcharge de l'opérateur ** (puissance) ;
__radd__     : commutativité
__iadd__     : Oppérateur += et -=

            COMPARAISON

==  :   def __eq__(self,objet_a_comparer):
!=  :   def __ne__(self,objet_a_comparer):
>   :   def __gt__(self,objet_a_comparer):
>=  :   def __ge__(self,objet_a_comparer):
<   :   def __lt__(self,objet_a_comparer):
<=  :   def __le__(self,objet_a_comparer):

"""

class ZDict :
    """ Classe enveloppe d'un dictionnaire """
    def __init__ ( self ):
        """ Notre classe n'accepte aucun param ÃƒÂ¨tre """
        self . _dictionnaire = {}

    def __getitem__ (self , index ):
        """ Cette mÃƒÂ© thode spÃƒÂ© ciale est appel ÃƒÂ©e quand on fait objet[index]
         Elle redirige vers self._dictionnaire[index]"""
        return self._dictionnaire[index]

    def __setitem__ (self , index , valeur ):
        """ Cette mÃƒÂ© thode est appel ÃƒÂ©e quand on ÃƒÂ© crit objet[index]=valeur
        On redirige vers self._dictionnaire[index]=valeur """
        self._dictionnaire[index] = valeur
#c=ZDict()

"""
    Si nous dÃƒÂ©finition __getitem__ et __setitem__ on poura faoir comporter laclasse
    comme un dictionnnnaire
"""
#c["d"]=76
#print(c["d"])

x=Vecteur(1,3)
y=Vecteur(6,1)
w=x+y
print(w)
##
##x.afficher()
##y.afficher()
##w=x+y
##y.afficher()