#This is the file which contains the Pokémon battle itself
#Date created 12/5/25
#I will put the combat in this file. This file will use resources from Charizard.py and other Pokémon files
#Imports
import random
import sys
import time
from Charizard import charizard1
from Charizard import charizard2
from Charizard import toolbox_charizard #Lists of the available moves
from Charizard import bellydrum_charizard
import Main
#'Toolbox Charizard' imports
from Charizard import flamethrower
from Charizard import solar_beam
from Charizard import air_slash
from Charizard import ancient_power
#'Belly Drum Charizard' imports
from Charizard import belly_drum
from Charizard import flare_blitz
from Charizard import acrobatics
from Charizard import metal_claw

#Lists
options = ['Battle', 'Switch']
#functions
def dramatic_effect(txt):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print('\n')

def damage_calculation(move, attacker, objective):
    damage = (2 * 50 / 5 + 2) * move.base_power * ()
#Main
player1_name = 'Ash'
player2_name = 'George Lucas'

dramatic_effect(f'A battle has started between {player1_name} and {player2_name}')
time.sleep(1.5)
p1_pkmn1 = charizard1
p2_pkmn_1 = charizard2
p1_active_pkmn = 'charizard'
p2_active_pkmn = 'charizard'
dramatic_effect(f"{player1_name}: '{p1_active_pkmn}, go!' ")
time.sleep(1)
dramatic_effect(f"{player2_name}: '{p2_active_pkmn}, go!' ")
time.sleep(1)
while True:
    if charizard1.hp == 0 and charizard2.hp == 0: #Victory and tie conditions use a function built into the Pokemon class itself
        dramatic_effect("Eh!? What's this!!?")
        dramatic_effect("Both active Pokémon are knocked out, It's a tie!!!")
        dramatic_effect('🎊🎉🎆')
    elif charizard1.hp == 0:
        dramatic_effect('The battle has come to an end!!!')
        dramatic_effect(f"{player1_name}'s {p1_active_pkmn} can no longer fight!!!")
        dramatic_effect(f"The winner is: 🏆🏆{player2_name}🏆🏆!!!")
        dramatic_effect('🎊🎊🎉🎉🎆🎆')
    elif charizard2.hp == 0:
        dramatic_effect('The battle has come to an end!!!')
        dramatic_effect(f"{player2_name}'s {p2_active_pkmn} can no longer fight!!!")
        dramatic_effect(f"The winner is: 🏆🏆{player1_name}🏆🏆!!!")
        dramatic_effect('🎊🎊🎉🎉🎆🎆')
    #Pokemon battle loop starts here
    #p1_turnchoice = input(dramatic_effect(f'{p1_activepkmn} is your active Pokemon, switch active pkmn or fight?'))
    dramatic_effect(f'{player1_name}, choose your move')

    for listed_move in toolbox_charizard:
        dramatic_effect(listed_move)
        time.sleep(0.5)
    p1_turnchoice = input('').lower()
    while p1_turnchoice not in toolbox_charizard:
        dramatic_effect('\x1B[3mYour Pokémon looks confused at you, as if it did not understand your comand\x1B[23m')
        p1_turnchoice = input(dramatic_effect(f'{player1_name}, choose your move')).lower()
    if 
        break
