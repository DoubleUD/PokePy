import Pokemon
def typeup()
    print(types)
    attacking = int(input("Attacking type?"))
    relationship = input("s/n/r/u") # Super effective/ Neutral/ Not very effective/ No effect
    sen = "p" #Sentinel Variable
    defendingl=[]
    while sen != "q":
        defending = input("Defending type(s)? Type q to quit") 
        if defending == "q":
            sen = defending
        else:
            defendingl.append(int(defending))

    relationships = {"s": 20, "n": 10, "r": 5, "u": 0}

    for i in defendingl:
        Pokemon.typechart[attacking][i]= relationships[relationship]

    print(Pokemon.typechart)


