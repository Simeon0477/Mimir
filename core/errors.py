class NoListError(Exception):
    def __init__(self):
        self.message = "The parameter 'data' should be a 'list'"
        super().__init__(self.message)

class NoEqualLengthError(Exception):
    def __init__(self):
        self.message = "The parameters 'x' and 'y' have differents lengths"
        super().__init__(self.message)
        
class VoidList(Exception):
    def __init__(self):
        self.message = "The list is voiod"
        super().__init__(self.message)