#Imports
import random
import sys
import time
from Pokédex import *
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
    chance = random.randint(10000)
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

#super_effective is an adaptation of how super effective hits work in the game. I feel like this function could be optimised, but I don't know if I have the time, and it seems to work well
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
    elif move.ptype == 'flying' and target.name == 'decidueye':
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
    else:
        return 1

#Damage calculation explained:
    #50 is the level of the attacking pkmn, but I chose to just put 50 since my program doesn't have any other interaction with the pkmn's level
    #This functions returns the damage a move does. It is the core of the battle system, so I must make sure it works properly
    #Damage of a move always varies between 100% and 85%
def damage_calculation(move, attacker, target):
    if move.category == 'special':
        damage = ((2 * 50 / 5 + 2) * move.base_power * (attacker.spatk / target.spdif) / 50 + 2) * crit_hit(move) * stab(move, attacker) * super_effective(move, target) * round(random.uniform(0.85, 1), 2)
        damage = round(damage)
        return damage
    elif move.category == 'physical':
        damage = ((2 * 50 / 5 + 2) * move.base_power * (attacker.atk / target.dif) / 50 + 2) * crit_hit(move) * stab(move, attacker) * super_effective(move, target) * round(random.uniform(0.85, 1), 2)
        damage = round(damage)
        return damage

damage_calculation(flamethrower, charizard1, decidueye1)
print()