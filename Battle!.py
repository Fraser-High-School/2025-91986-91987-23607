#Imports
import random
import sys
import time
from Pokédex import *
from Main import *
#Lists
#functions
#dramatic_effect prints one by one, which is very neat 
def dramatic_effect(txt):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print('\n')
#crit_hit is an adaptation of how critical hits work in the original game. most moves have a critical hit chance of 4.17%, while a few have 12.5% or more.
#a critical hit is when an attack does more damage than it is supposed to do by pure randomness.
def crit_hit(move):
    security_chech = hasattr(move, 'crit_rate')
    if security_chech == False:
        return "error: the move selected (if any) does not have a critical hit rate"
    chance = random.randint(1, 10000)
    if chance <= 417:
        return 1.5
    elif (move).crit_rate == 1250 and chance <= 1250:
        return 1.5
    else:
        return 1.0

#"stab" (Same Type Attack Bounus) is a function that increases damage output if the Pokémon has the same type as the attack it is using
def stab(move, attacker):
    security_chech = hasattr(move, 'ptype')
    if security_chech == False:
        return "error: the move selected (if any) does not have attribute 'ptype'"
    if move.ptype in attacker.typing:
        return 1.5
    else:
        return 1

#super_effective is an adaptation of how super effective hits work in the game. I feel like this function could be optimised, but I don't know if I have the time, and it seems to work well
#This function returns a value between 0.25 and 4, which is then used as a multiplier in damage_calculation
def super_effective(move, target):
    effectiveness = 1
    security_chech = hasattr(move, 'ptype')
    if security_chech == False:
        return "error: the move selected (if any) does not have attribute 'ptype'"
    #Fire type interactions
    if move.ptype == 'fire':
        if 'grass' in target.typing:
            effectiveness = effectiveness * 2
        if 'water' or 'fire' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    #Dark type interactions
    elif move.ptype == 'dark':
        if 'fairy' or 'fighting' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    #Water type interactions
    elif move.ptype == 'water':
        if 'fire' in target.typing:
            effectiveness = effectiveness * 2
        if 'water' or 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    #Grass type interactions
    elif move.ptype == 'grass':
        if 'water' or'ground' in target.typing:
                effectiveness = effectiveness * 2
        if 'grass' or 'flying' or 'fire' in target.typing:
                effectiveness = effectiveness * 0.5
        return effectiveness
    #Fairy type interactions
    elif move.ptype == 'fairy':
        if 'fairy' or 'fire' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'fighting' in target.typing:
            effectiveness = effectiveness * 2
        return effectiveness
    #Flying type interactions
    elif move.ptype == 'flying':
        if 'grass' in target.typing:
            effectiveness = effectiveness * 2
        if 'fighting' in target.typing:
            effectiveness = effectiveness * 2
        return effectiveness
    #ground type interactions
    elif move.ptype == 'ground':
        if 'flying' in target.typing:
            effectiveness = 0
        if 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    #Steel type interactions
    elif move.ptype == 'steel':
        if 'fairy' in target.typing:
            effectiveness = effectiveness * 2
        if 'fire' or 'fighting' or 'water' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
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
        return effectiveness
    #Fighting type interactions
    elif move.ptype == 'fighting':
        if 'fairy' or 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'flying' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    #Ice type interactions
    elif move.ptype == 'ice':
        if 'flying' in target.typing:
            effectiveness = effectiveness * 2
        if 'fire' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    #electric type interactions
    elif move.ptype == 'electric':
        if 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'ground' in target.typing:
            effectiveness = 0
        if 'flying' in target.typing:
            effectiveness = effectiveness * 2
        return effectiveness
    else: #This covers neutral and unexpected cases of type interactions
        return effectiveness

#Damage calculation explained:
    #50 is the level of the attacking pkmn, but I chose to just put 50 since my program doesn't have any other interaction with the pkmn's level
    #This functions returns the damage a move does. It is the core of the battle system, so I must make sure it works properly
    #Damage of a move always varies between 100% and 85%
def damage_calculation(move, attacker, target):
    security_check = hasattr(attacker, 'hp')
    if security_check == False:
        return "attacker (if any) has no hp attribute, thus, it is not a Pokémon" #Error message to detect if a Pokémon is being used as an attacker in the damage calculation
    if move.category == 'special':
        damage = ((2 * 50 / 5 + 2) * move.base_power * (attacker.spatk / target.spdif) / 50 + 2) * crit_hit(move) * stab(move, attacker) * super_effective(move, target) * round(random.uniform(0.85, 1), 2)
        damage = round(damage)
        return damage
    elif move.category == 'physical':
        damage = ((2 * 50 / 5 + 2) * move.base_power * (attacker.atk / target.dif) / 50 + 2) * crit_hit(move) * stab(move, attacker) * super_effective(move, target) * round(random.uniform(0.85, 1), 2)
        damage = round(damage)
        return damage

#Main
player1_name = 'Ash'
player2_name = 'George Lucas'
dramatic_effect(f'A battle has started between {player1_name} and {player2_name}')
time.sleep(1.5)
p1_pkmn1 = charizard1
p2_pkmn1 = charizard2
p1_active_pkmn = charizard1
p2_active_pkmn = charizard2
dramatic_effect(f"{player1_name}: '{p1_active_pkmn}, go!' ")
time.sleep(1)
dramatic_effect(f"{player2_name}: '{p2_active_pkmn}, go!' ")
winsound.PlaySound('battle music.wav', winsound.SND_ASYNC)
time.sleep(1)
while charizard1.hp > 0 or charizard2.hp > 0:
    #Pokemon battle loop starts here
    dramatic_effect(f'{player1_name}, choose your move')
    for listed_move in toolbox_charizard:
        dramatic_effect(listed_move)
        time.sleep(0.5)
    p1_turnchoice = input('Choose ').lower()
    while p1_turnchoice not in toolbox_charizard:
        dramatic_effect('\x1B[3mYour Pokémon looks confused at you, as it did not understand your comand\x1B[23m')
        p1_turnchoice = input(dramatic_effect(f'{player1_name}, choose your move')).lower()
    if p1_turnchoice == toolbox_charizard[0]:



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