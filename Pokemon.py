import Data
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
        self.type = (Data.types[type1], Data.types[type2])
        self.growth = growth
        self.evo = evo

class Mon:

    def __init__(self, species, iv, ev, ability, moveset, nature, lvl, frnd, item, shiny, gender, id, name = species, isegg = False):
        self.species = species
        self.iv = iv
        self.ev = ev
        self.ability = ability
        self.moveset = moveset
        self.nature = nature
        self.lvl = lvl
        self.friend = frnd
        self.item = item
        self.shiny = shiny
        self.gender = gender
        self.name = name
        self.id = id
        self.exp = Data.exptable[lvl][self.species.growth]


        self.hp = int((((2 * self.species.hp) + self.iv[0] + (self.ev[0]/4)) * self.lvl /100) + self.lvl + 10)

        self.attack = int(((((2 * self.species.attack) + self.iv[1] + (self.ev[1]/4)) * self.lvl /100) + 5) * \
                   Data.natures[self.nature][0])

        self.defense = int(((((2 * self.species.defense) + self.iv[2] + (self.ev[2] / 4)) * self.lvl / 100) + 5) * \
                   Data.natures[self.nature][1])

        self.spattack = int(((((2 * self.species.spattack) + self.iv[3] + (self.ev[3] / 4)) * self.lvl / 100) + 5) * \
                   Data.natures[self.nature][2])

        self.spdefense = int(((((2 * self.species.spdefense) + self.iv[4] + (self.ev[4] / 4)) * self.lvl / 100) + 5) * \
                   Data.natures[self.nature][3])

        self.speed = int(((((2 * self.species.speed) + self.iv[5] + (self.ev[5] / 4)) * self.lvl / 100) + 5) * \
                   Data.natures[self.nature][4])

    def updatestats(self, hp = True, attack = True, defense = True, spattack = True, spdefense = True, speed = True):
        if hp == True:
            self.hp = int((((2 * self.species.hp) + self.iv[0] + (self.ev[0] / 4)) * self.lvl / 100) + self.lvl + 10)
        if attack == True:
            self.attack = int(((((2 * self.species.attack) + self.iv[1] + (self.ev[1] / 4)) * self.lvl / 100) + 5) * \
                              Data.natures[self.nature][0])
        if defense == True:
            self.defense = int(((((2 * self.species.defense) + self.iv[2] + (self.ev[2] / 4)) * self.lvl / 100) + 5) * \
                               Data.natures[self.nature][1])
        if spattack == True:
            self.spattack = int(((((2 * self.species.spattack) + self.iv[3] + (self.ev[3] / 4)) * self.lvl / 100) + 5) * \
                                Data.natures[self.nature][2])
        if spdefense == True:
            self.spdefense = int(
                ((((2 * self.species.spdefense) + self.iv[4] + (self.ev[4] / 4)) * self.lvl / 100) + 5) * \
                Data.natures[self.nature][3])
        if speed == True:
            self.speed = int(((((2 * self.species.speed) + self.iv[5] + (self.ev[5] / 4)) * self.lvl / 100) + 5) * \
                             Data.natures[self.nature][4])


    def checklvlup(self):
        if self.lvl != 100:
            if Data.exptable[self.lvl+1][self.species.growth] <= self.exp:
                self.lvl += 1
                self.updatestats()
                self.checklvlup()

class BattleMon(Mon):

    def __init__(self,species, iv, ev, ability, moveset, nature, exp, frnd, item, shiny, gender, name, id, currentHP):

        Mon.__init__(self,species, iv, ev, ability, moveset, nature, exp, frnd, item, shiny, gender, name, id)
        self.maxhp = self.hp
        self.currenthp = self.maxhp
        self.buffs = [0,0,0,0,0]


class Player:
    import random
    def __init__(self, name, id=random.randint(0, 999999), party = [], pc = [], bag = [], money = 0):

        self.name = name
        self.id = id
        self.party = party
        self.pc = pc
        self.bag = bag
        self.money = money

    def addpoke(self, pokemon):

        if isinstance(pokemon, Mon):
            if length(self.party) < 6:
                self.party.append(pokemon)
            else:
                self.pc.append(pokemon)
        else:
            print("That's not a Pokémon!")

    def additem(self, item):
        self.bag.append(item)

    def addmoney(self, amount):
        self.money += amount
        if self.money > 999999:
            money = 999999

    def takemoney(self, amount):
        self.money -= amount
        if self.money < 0:
            money = 0


