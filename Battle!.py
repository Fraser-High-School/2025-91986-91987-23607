#This is the file which contains the Pokémon battle itself
#Date created 12/5/25
#I will put the combat in this file. This file will use resources from Charizard.py and other Pokémon files
#Imports
import random
import sys
import time
from Charizard import *
from playsound import playsound
#Lists
options = ['Battle', 'Switch']
#functions
def dramatic_effect(txt):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print('\n')
#crit_hit is an adaptation of how critical hits work in the original game. most moves have a critical hit chance of 4.17%, while a few have 12.5% or more.
#This function is a simplified version of the critical hit system used in actual Pokémon games.
def crit_hit(move):
    chance = random.randit(10000)
    if chance <= 417:
        return 1.5
    elif (move).crit_rate == 1250 and chance <= 1250:
        return 1.5
    else:
        return 1.0
#"stab" (Same Type Attack Bounus) is a function that increases damage output if the Pokémon has the same type as the attack it is using
def stab(move, attacker):
    if any(move.ptype == attacker.type1 or move.ptype == attacker.type2 for x in (attacker.type1, attacker.type2, move.ptype)):
        return 1.5
#Damage calculation explained:
    #50 is the level of the attacking pkmn, but I chose to just put 50 since my program doesn't have any other interaction with the pkmn's level
    #This functions returns the damage a move does. It is the core of the battle system, so I must make sure it works properly
def damage_calculation(move, attacker, target):
    if move.category == 'special'
        damage = ((2 * 50 / 5 + 2) * move.base_power * (atacker.spatk / target.spdif) / 50 + 2) * crit_hit(move) * stab(move, attacker) #*super_effective
        damage = round(damage)
        return damage
    elif move.category == 'physical'
        damage = ((2 * 50 / 5 + 2) * move.base_power * (atacker.atk / target.dif) / 50 + 2) * crit_hit(move) stab(move, attacker) #*super_effective
        damage = round(damage)
        return damage
#Main
player1_name = 'Ash'
player2_name = 'George Lucas'
#I decided to start with a 1v1 Charizard duel first, and then expand it to support more Pokemon and modes
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
while charizard1.hp > 0 or charizard2.hp > 0:
    #Pokemon battle loop starts here
    #p1_turnchoice = input(dramatic_effect(f'{p1_activepkmn} is your active Pokemon, switch active pkmn or fight?'))
    dramatic_effect(f'{player1_name}, choose your move')
    for listed_move in toolbox_charizard:
        dramatic_effect(listed_move)
        time.sleep(0.5)
    p1_turnchoice = input('Choose').lower()
    while p1_turnchoice not in toolbox_charizard:
        dramatic_effect('\x1B[3mYour Pokémon looks confused at you, as it did not understand your comand\x1B[23m')
        p1_turnchoice = input(dramatic_effect(f'{player1_name}, choose your move')).lower()
    if p1_turnchoice == 'Flamethrower':


#This part happens only if one pkmn is KO'd
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