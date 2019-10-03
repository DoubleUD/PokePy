
class Species:

    def __init__(self, dex, name, stats, type1, type2, evo, abilities, movepool, growth):
        self.dex = dex
        self.species = name
        self.stats = stats
        self.hp = self.stats[0]
        self.attack = self.stats[1]
        self.defense = self.stats[2]
        self.spattack = self.stats[3]
        self.spdefense = self.stats[4]
        self.speed = self.stats[5]
        self.type = (types[type1], types[type2])
        self.evo = evo
        self.abilities = abilities
        self.movepool = movepool
        self.growth = growth


class Mon:

    def __init__(self, species, iv, ev, ability, moveset, nature, exp, frnd, item, shiny, gender, name, id,):
        self.species = species
        self.iv = iv
        self.ev = ev
        self.ability = ability
        self.moveset = moveset
        self.nature = nature
        self.exp = exp
        self.friend = frnd
        self.item = item
        self.shiny = shiny
        self.gender = gender
        self.name = name
        self.id = id
        self.hp = species.hp + self.iv[1]
