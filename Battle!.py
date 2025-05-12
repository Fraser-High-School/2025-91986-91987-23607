#I will put the combat in this file. This file will use resources from Charizard.py and other Pokémon files
#Imports
import random
import sys
import time
import Charizard
#functions
def dramatic_effect(txt):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print('\n')
#Main
player1_name = 'Ash'
player2_name = 'George Lucas'

dramatic_effect(f'A battle has started between {player1_name} and {player2_name}')
p1_pkmn1 = 'charizard'
p1_pkmn1_moveset = toolbox_charizard
p2_pkmn_1 = 'charizard'
