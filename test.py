import Pokemon
import Data

Bulbasaur = Pokemon.Species(1,"Bulbasaur", [45, 49, 49, 65, 65, 45], 12, 3, "Ivysaur",[],[],3)
A1 = Pokemon.Mon(Bulbasaur, [31,31,31,31,31,31], [0,152,0,0,100,252], 1, [0,1,2,3,4], "Bold", 1, 0, 1, False, 8, 4466)
print(A1.hp)
print(A1.name)
def pt():
    print(A1.exp)
    A1.exp += 20000
    A1.checklvlup()
    print(A1.lvl)
pt()
print(A1.hp, A1.attack, A1.defense, A1.spattack, A1.spdefense, A1.speed)



