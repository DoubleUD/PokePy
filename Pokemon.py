types = {0: 'Normal', 1: 'Fighting', 2: 'Flying', 3: 'Poison', 4: 'Ground', 5: 'Rock', 6: 'Bug', 7: 'Ghost', 8: 'Steel',
         9: '???', 10: 'Fire', 11: 'Water', 12: 'Grass', 13: 'Electric', 14: 'Psychic', 15: 'Ice', 16: 'Dragon',
         17: 'Dark', 18: "Fairy"}

natures = { 'Adamant':[1,3], 'Brave':[1,5], 'Lonely':[1,2], 'Naughty':[1,4], 'Bold':[2,1], 'Lax':[2,4], 'Relaxed':[2,5],
            'Impish':[2,3],'Timid':[5,1], 'Hasty':[5,2], 'Jolly':[5,3],'Naive':[5,4], 'Mild':[3,2], 'Quiet':[3,5],
            'Rash':[3,4], 'Modest':[3,1], 'Gentle':[4,2], 'Calm':[4,1], 'Sassy':[4,5], 'Careful':[4,3], 'Hardy':[0,0],
            'Docile':[0,0],'Serious':[0,0], 'Bashful':[0,0], 'Quirky':[0,0]}


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


typechart= [[10, 10, 10, 10, 10,  5, 10, 00,  5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [20, 10,  5,  5, 10, 20,  5, 00, 20, 10, 10, 10, 10, 10,  5, 20, 10, 20,  5],
            [10, 10, 10, 10, 10,  5, 20, 10,  5, 10, 10, 10, 20,  5, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  5, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]


class Move:

    def __init__(self,name,type,power,accuracy,category, effect):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.cat = category
        self.effect = effect


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
