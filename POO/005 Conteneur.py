class ZDict :
    """ Classe enveloppe d'un dictionnaire """
    def __init__ ( self ):
        """ Notre classe n'accepte aucun param ètre """
        self . _dictionnaire = {}

    def __getitem__ (self , index ):
        """ Cette mé thode spé ciale est appel ée quand on fait objet[index]
         Elle redirige vers self._dictionnaire[index]"""
        return self._dictionnaire[index]

    def __setitem__ (self , index , valeur ):
        """ Cette mé thode est appel ée quand on é crit objet[index]=valeur
        On redirige vers self._dictionnaire[index]=valeur """
        self._dictionnaire[index] = valeur
c=ZDict()

"""
    Si nous définition __getitem__ et __setitem__ on poura faoir comporter laclasse
    comme un dictionnnnaire
"""
c["d"]=76
print(c["d"])