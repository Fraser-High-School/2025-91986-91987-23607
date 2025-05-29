# imports
#from playsound import playsound
from Charizard import *
#functions
def super_effective(move, target):
    #Fire type interactions
    if move.ptype == 'fire' and target.type1 == 'grass':
        return 2
    elif move.ptype == 'fire' and target.type1 == 'water':
        return 0.5
    #Dark type interactions
    elif move.ptype == 'dark' and target.type1 == 'fairy' or move.ptype == 'dark' and target.type2 == 'fighting'
    elif move.ptype == 'water' and target.type1 ==
    elif move.ptype == 'grass' and target.type1 ==
    elif move.ptype == 'fairy' and target.type1 ==
    elif move.ptype == 'flying' and target.type1 ==
    elif move.ptype == 'fire' and target.type1 ==
    elif move.ptype == 'fire' and target.type1 ==
    elif move.ptype == 'fire' and target.type1 ==
#Test case