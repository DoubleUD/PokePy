
#methods to be added

class Move:

    def __init__(self,name,type,power,accuracy,category, pp, effect = None):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.cat = category
        self.pp = pp
        self.effect = effect
