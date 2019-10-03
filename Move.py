
#methods to be added

class Move:

    def __init__(self, name, type, power, accuracy, category, effect, target = opponent):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.cat = category
        self.effect = effect
        self.target = target
