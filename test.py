#Imports
from Pokédex import *
#Functions
def super_effective(move, target):
    effectiveness = 1
    if move.ptype == 'fire' and 'grass' in target.typing:
        effectiveness = effectiveness * 2
    return effectiveness
#Main
a = super_effective(flamethrower, decidueye1)
print(a)