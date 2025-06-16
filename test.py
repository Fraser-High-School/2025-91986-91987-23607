#Imports
from Pokédex import *
#Functions
def super_effective(move, target):
    effectiveness = 1
    #Fire type interactions
    if move.ptype == 'fire':
        if 'grass' in target.typing:
            effectiveness = effectiveness * 2
        if 'water' or 'fire' in target.typing:
            effectiveness = effectiveness * 0.5
    #Dark type interactions
    elif move.ptype == 'dark':
        if 'fairy' or 'fighting' in target.typing:
            effectiveness = effectiveness * 0.5
    #Water type interactions
    elif move.ptype == 'water':
        if 'fire' in target.typing:
            effectiveness = effectiveness * 2
        if 'water' or 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
    #Grass type interactions
    elif move.ptype == 'grass':
        if 'water' or'ground' in target.typing:
                effectiveness = effectiveness * 2
        if 'grass' or 'flying' or 'fire' in target.typing:
                effectiveness = effectiveness * 0.5
    #Fairy type interactions
    elif move.ptype == 'fairy':
        if 'fairy' or 'fire' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'fighting' in target.typing:
            effectiveness = effectiveness * 2
    #Flying type interactions
    elif move.ptype == 'flying':
        if 'grass' or 'fighting' in target.typing:
            effectiveness = effectiveness * 2
    #ground type interactions
    elif move.ptype == 'ground':
        if 'flying' in target.typing:
        return 0
        if 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
    #Steel type interactions
    elif move.ptype == 'steel':
        if 'fairy' in target.typing:
            effectiveness = effectiveness * 2
        if 'fire' or 'fighting' or 'water' in target.typing:
            effectiveness = effectiveness * 0.5
    #Rock type interactions
    elif move.ptype == 'rock':
        if 'water' or 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'fire' in target.typing:
            effectiveness = effectiveness * 2
        if 'flying' in target.typing:
            effectiveness = effectiveness * 2
        if 'fighting' in target.typing:
            effectiveness = effectiveness * 0.5
    #Fighting type interactions
    elif move.ptype == 'fighting':
        if 'fairy' or 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'flying' in target.typing:
            effectiveness = effectiveness * 0.5
    #Ice type interactions
    elif move.ptype == 'ice':
        if 'flying' in target.typing:
            effectiveness = effectiveness * 2
        if 'fire' in target.typing:
            effectiveness = effectiveness * 0.5
    #electric type interactions
    elif move.ptype == 'electric':
        if 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'ground' in target.typing:
        return 0
        if 'flying' in target.typing:
            effectiveness = effectiveness * 2
    return effectiveness
#Main
a = super_effective(flamethrower, charizard1)
print(a)