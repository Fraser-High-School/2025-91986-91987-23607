# imports
#from playsound import playsound
from Charizard import *
#functions
def super_effective(move, target):
    #Fire type interactions
    if move.ptype == 'fire' and target.type1 == 'grass':
        return 2
    elif move.ptype == 'fire' and target.type1 == 'water' or move.ptype == 'fire' and target.type1 == 'fire':
        return 0.5
    #Dark type interactions
    elif move.ptype == 'dark' and target.type1 == 'fairy' or move.ptype == 'dark' and target.type2 == 'fighting':
        return 0.5
    #Water type interactions
    elif move.ptype == 'water' and target.type1 == 'fire':
        return 2
    elif move.ptype == 'water' and target.type1 == 'water' or move.ptype == 'water' and target.type1 == 'grass':
        return 0.5
    #Grass type interactions
    elif move.ptype == 'grass' and target.name == 'swampert':
        return 4
    elif move.ptype == 'grass' and target.type1 == 'grass' or target.name == 'togekiss':
        return 0.5
    elif move.ptype == 'grass' and target.name == 'charizard':
        return 0.25
    #Fairy type interactions
    elif move.ptype == 'fairy' and target.type1 == 'fairy' or move.ptype == 'fairy' and target.type1 == 'fire':
        return 0.5
    elif move.ptype == 'fairy' and target.type2 == 'fighting':
        return 2
    #Flying type interactions
    elif move.ptype == 'flying' and target.name == 'decidueye'
        return 4
    #ground type interactions
    elif move.ptype == 'ground' and target.type2 == 'flying':
        return 0
    elif move.ptype == 'ground' and target.type1 == 'grass':
        return 0.5
    #Steel type interactions
    elif move.ptype == 'steel' and target.type1 == 'fairy':
        return 2
    elif move.ptype == 'steel' and target.type1 == 'fire' or move.ptype == 'steel' and target.type2 == 'fighting' or move.ptype == 'steel' and target.type1 == 'water':
        return 0.5
    #Rock type interactions
    elif move.ptype == 'rock' and target.type1 == 'water':
        return 0.5
    elif move.ptype == 'rock' and target.name == 'charizard':
        return 4
    elif move.ptype == 'rock' and target.name == 'togekiss':
        return 2
    elif move.ptype == 'rock' and target.name == 'decidueye':
        return 0.25
    #Fighting type interactions
    elif move.ptype == 'fighting' and target.type1 == 'fairy' or move.ptype == 'fighting' and target.type1 == 'grass':
        return 0.5
    #Ice type interactions
    elif move.ptype == 'ice' and target.name == 'Togekiss':
        return 2
    #electric type interactions
    elif move.ptype == 'electric' and target.type1 == 'grass':
        return 0.5
    elif move.ptype == 'electric' and target.type2 == 'ground':
        return 0
    elif move.ptype == 'electric' and target.type2 == 'flying':
        return 2
#Test case