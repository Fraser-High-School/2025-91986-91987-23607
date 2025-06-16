#Imports
from Pokédex import *
#Functions
def super_effective(move, target):
    effectiveness = 1
    #Fire type interactions
    if move.ptype == 'fire' and 'grass' in target.typing:
        effectiveness = effectiveness * 2
    if move.ptype == 'fire' and 'water' or 'fire' in target.typing:
        effectiveness = effectiveness * 0.5
    #Dark type interactions
    if move.ptype == 'dark' and 'fairy' or 'fighting' in target.typing:
        effectiveness = effectiveness * 0.5
    #Water type interactions
    if move.ptype == 'water' and 'fire' in target.typing:
        effectiveness = effectiveness * 2
    if move.ptype == 'water' and 'water' or 'grass' in target.typing:
        effectiveness = effectiveness * 0.5
    #Grass type interactions
    if move.ptype == 'grass' and 'water' or'ground' in target.typing:
        effectiveness = effectiveness * 2
    if move.ptype == 'grass' and 'grass' or 'flying' or 'fire' in target.typing:
        effectiveness = effectiveness * 0.5
    #Fairy type interactions
    if move.ptype == 'fairy' and 'fairy' or 'fire' in target.typing:
        effectiveness = effectiveness * 0.5
    if move.ptype == 'fairy' and 'fighting' in target.typing:
        effectiveness = effectiveness * 2
    #Flying type interactions
    if move.ptype == 'flying' and 'grass' or 'fighting' in target.typing:
        effectiveness = effectiveness * 2
    #ground type interactions
    if move.ptype == 'ground' and 'flying' in target.typing:
        return 0
    if move.ptype == 'ground' and 'grass' in target.typing:
        effectiveness = effectiveness * 0.5
    #Steel type interactions
    if move.ptype == 'steel' and 'fairy' in target.typing:
        effectiveness = effectiveness * 2
    if move.ptype == 'steel' and 'fire' or 'fighting' or 'water' in target.typing:
        effectiveness = effectiveness * 0.5
    #Rock type interactions
    if move.ptype == 'rock' and 'water' or 'grass' in target.typing:
        effectiveness = effectiveness * 0.5
    if move.ptype == 'rock' and 'fire' in target.typing:
        effectiveness = effectiveness * 2
    if move.ptype == 'rock' and 'flying' in target.typing:
        effectiveness = effectiveness * 2
    if move.ptype == 'rock' and 'fighting' in target.typing:
        effectiveness = effectiveness * 0.5
    #Fighting type interactions
    if move.ptype == 'fighting' and 'fairy' or 'grass' in target.typing:
        effectiveness = effectiveness * 0.5
    if move.ptype == 'fighting' and 'flying' in target.typing:
         effectiveness = effectiveness * 0.5
    #Ice type interactions
    if move.ptype == 'ice' and 'flying' in target.typing:
        effectiveness = effectiveness * 2
    if move.ptype == 'ice' and 'fire' in target.typing:
        effectiveness = effectiveness * 0.5
    #electric type interactions
    if move.ptype == 'electric' and 'grass' in target.typing:
        effectiveness = effectiveness * 0.5
    if move.ptype == 'electric' and 'ground' in target.typing:
        return 0
    if move.ptype == 'electric' and 'flying' in target.typing:
        effectiveness = effectiveness * 2
    return effectiveness
#Main
a = super_effective(flamethrower, charizard1)
print(a)