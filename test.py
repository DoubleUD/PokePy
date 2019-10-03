import Pokemon

Bulbasaur = Pokemon.Species(1,"Bulbasaur", [45, 49, 49, 65, 65, 45], 12, 3, "Ivysaur",[],[],"g")
A1 = Pokemon.Mon(Bulbasaur, [31,31,31,31,31,31], [0,0,0,0,0,0], 1, [0,1,2,3,4], "Bold", 300, 0, 1, False, 8, "Budley", 4466)
print(A1.hp)
print(Pokemon.typechart)
def pt():
    print(5)


Tackle = Pokemon.Move("Tackle", 0, 40, 100, 0, pt())

Tackle.effect
