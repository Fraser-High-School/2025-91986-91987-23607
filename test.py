#Imports
from Pokédex import *
#Functions
def super_effective(move, target):
    effectiveness = 1
    #Fire type interactions
    if move.ptype == 'fire' and target.type1 == 'grass':
        effectiveness = effectiveness * 2
    if move.ptype == 'fire' and target.type1 == 'water' or move.ptype == 'fire' and target.type1 == 'fire':
        effectiveness = effectiveness * 0.5
    #Dark type interactions
    if move.ptype == 'dark' and target.type1 == 'fairy' or move.ptype == 'dark' and target.type2 == 'fighting':
        effectiveness = effectiveness * 0.5
    #Water type interactions
    if move.ptype == 'water' and target.type1 == 'fire':
        effectiveness = effectiveness * 2
    if move.ptype == 'water' and target.type1 == 'water' or move.ptype == 'water' and target.type1 == 'grass':
        effectiveness = effectiveness * 0.5
    #Grass type interactions
    if move.ptype == 'grass' and target.type1 == 'water':
        effectiveness = effectiveness * 2
    if move.ptype == 'grass' and target.type1 == 'grass' or move.ptype == 'grass' and target.type2 == 'flying':
        effectiveness = effectiveness * 0.5
    if move.ptype == 'grass' and target.type1 == 'fire':
        effectiveness = effectiveness * 0.5
    if move.ptype == 'grass' and target.type2 == 'ground':
        effectiveness = effectiveness * 2
    #Fairy type interactions
    if move.ptype == 'fairy' and target.type1 == 'fairy' or move.ptype == 'fairy' and target.type1 == 'fire':
        effectiveness = effectiveness * 0.5
    if move.ptype == 'fairy' and target.type2 == 'fighting':
        effectiveness = effectiveness * 2
    #Flying type interactions
    if move.ptype == 'flying' and target.type1 == 'grass':
        effectiveness = effectiveness * 2
    if move.ptype == 'flying' and target.type2 == 'fighting':
        effectiveness = effectiveness * 2
    #ground type interactions
    if move.ptype == 'ground' and target.type2 == 'flying':
        return 0
    if move.ptype == 'ground' and target.type1 == 'grass':
        effectiveness = effectiveness * 0.5
    #Ste type interactions
    if move.ptype == 'ste' and target.type1 == 'fairy':
        effectiveness = effectiveness * 2
    if move.ptype == 'ste' and target.type1 == 'fire' or move.ptype == 'ste' and target.type2 == 'fighting' or move.ptype == 'ste' and target.type1 == 'water':
        effectiveness = effectiveness * 0.5
    #Rock type interactions
    if move.ptype == 'rock' and target.type1 == 'water':
        effectiveness = effectiveness * 0.5
    if move.ptype == 'rock' and target.type1 == 'fire':
        effectiveness = effectiveness * 2
    if move.ptype == 'rock' and target.type2 == 'flying':
        effectiveness = effectiveness * 2
    if move.ptype == 'rock' and target.type2 == 'fighting':
        effectiveness = effectiveness * 0.5
    if move.ptype == 'rock' and target.type1 == 'grass':
        effectiveness = effectiveness * 0.5
    #Fighting type interactions
    if move.ptype == 'fighting' and target.type1 == 'fairy' or move.ptype == 'fighting' and target.type1 == 'grass':
        effectiveness = effectiveness * 0.5
    #Ice type interactions
    if move.ptype == 'ice' and target.type2 == 'flying':
        effectiveness = effectiveness * 2
    if move.ptype == 'ice' and target.type1 == 'fire':
        effectiveness = effectiveness * 0.5
    #ectric type interactions
    if move.ptype == 'ectric' and target.type1 == 'grass':
        effectiveness = effectiveness * 0.5
    if move.ptype == 'ectric' and target.type2 == 'ground':
        return 0
    if move.ptype == 'ectric' and target.type2 == 'flying':
        effectiveness = effectiveness * 2
    return effectiveness

#Main
a = super_effective(flamethrower, decidueye1) #And air slash
print(a)