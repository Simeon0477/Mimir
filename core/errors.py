"""
   Erreur rencontrée lorsque l'utilisateur donne en paramètre
   une variable n'étant pas une chaine de caractère 
"""
class NoListError(Exception):
    def __init__(self):
        self.message = "The parameter 'data' should be a 'list'"
        super().__init__(self.message)


"""
   Erreur rencontrée lorsque l'utilisateur donne en paramètre
   deux listes qui n'ont pas la même longueur
"""
class NoEqualLengthError(Exception):
    def __init__(self):
        self.message = "The parameters 'x' and 'y' have differents lengths"
        super().__init__(self.message)
        
        
"""
   Erreur rencontrée lorsque l'utilisateur donne en paramètre
   une liste vide.
"""
class VoidList(Exception):
    def __init__(self):
        self.message = "The list is voiod"
        super().__init__(self.message)