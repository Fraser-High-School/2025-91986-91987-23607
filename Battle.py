#Imports
import random
import sys
import time
from Pokédex import *
import winsound
import pygame
#Lists
#Functions


def dramatic_effect(txt):
    """Type characters of a given string one by one.

    It uses a loop and functions imported from sys to print characters
    in a given string, one by one, while also adding spacing at the end.
    """
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    print('\n')


def p(strin):
    print(f'{strin}\n')

def crit_hit(move):
    """Choose a random number from 1 to 10K> If it is smaller than the argument's critical hit ratio, return 1.5

    crit_hit is an adaptation of how critical hits work in the original game.
    Most moves have a critical hit chance of 4.17%, while a few have 12.5% or more.
    a critical hit is when an attack does more damage than it is supposed to do by pure randomness."""
    security_chech = hasattr(move, 'crit_rate')
    if security_chech is False:
        return "error: the move selected (if any) does not have a critical hit rate"
    chance = random.randint(1, 10000)
    if chance <= move.crit_rate:
        return 1.5
    else:
        return 1.0


def stab(move, attacker):
    """"stab" (Same Type Attack Bounus) is a function that increases
    damage output if the Pokémon has the same type as the attack it is using
    """
    security_chech = hasattr(move, 'ptype')
    if security_chech is False:
        return "error: the move selected (if any) does not have attribute 'ptype'"
    if move.ptype in attacker.typing:
        return 1.5
    else:
        return 1


def super_effective(move, target):
    """super_effective is an adaptation of how super effective hits work
    in the game. I feel like this function could be optimised, but I don't know
    if I have the time, and it seems to work well. This function returns a value
    between 0.25 and 4, which is then used as a multiplier in damage_calculation
    """
    effectiveness = 1
    security_chech = hasattr(move, 'ptype')
    if security_chech is False:
        return "error: the move selected (if any) does not have attribute 'ptype'"
    # Fire type interactions
    if move.ptype == 'fire':
        if 'grass' in target.typing:
            effectiveness = effectiveness * 2
        if 'water' or 'fire' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    # Dark type interactions
    elif move.ptype == 'dark':
        if 'fairy' or 'fighting' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    # Water type interactions
    elif move.ptype == 'water':
        if 'fire' in target.typing:
            effectiveness = effectiveness * 2
        if 'water' or 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    # Grass type interactions
    elif move.ptype == 'grass':
        if 'water' or'ground' in target.typing:
                effectiveness = effectiveness * 2
        if 'grass' or 'flying' or 'fire' in target.typing:
                effectiveness = effectiveness * 0.5
        return effectiveness
    # Fairy type interactions
    elif move.ptype == 'fairy':
        if 'fairy' or 'fire' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'fighting' in target.typing:
            effectiveness = effectiveness * 2
        return effectiveness
    # Flying type interactions
    elif move.ptype == 'flying':
        if 'grass' in target.typing:
            effectiveness = effectiveness * 2
        if 'fighting' in target.typing:
            effectiveness = effectiveness * 2
        return effectiveness
    # ground type interactions
    elif move.ptype == 'ground':
        if 'flying' in target.typing:
            effectiveness = 0
        if 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    # Steel type interactions
    elif move.ptype == 'steel':
        if 'fairy' in target.typing:
            effectiveness = effectiveness * 2
        if 'fire' or 'fighting' or 'water' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    # Rock type interactions
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
    # Fighting type interactions
    elif move.ptype == 'fighting':
        if 'fairy' or 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'flying' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    # Ice type interactions
    elif move.ptype == 'ice':
        if 'flying' in target.typing:
            effectiveness = effectiveness * 2
        if 'fire' in target.typing:
            effectiveness = effectiveness * 0.5
        return effectiveness
    # electric type interactions
    elif move.ptype == 'electric':
        if 'grass' in target.typing:
            effectiveness = effectiveness * 0.5
        if 'ground' in target.typing:
            effectiveness = 0
        if 'flying' in target.typing:
            effectiveness = effectiveness * 2
        return effectiveness
    else: # This covers neutral and unexpected cases of type interactions
        return effectiveness


def damage_calculation(move, attacker, target):
    """Damage calculation explained:

    50 is the level of the attacking pkmn, but I chose to just put 50
    as my program doesn't have any other interaction with the pkmn's level.
    This functions returns the damage a move does. It is the core of the
    battle system, so I must make sure it works properly. Damage of a move
    always varies between 100% and 85%"""
    security_check = hasattr(attacker, 'hp')
    if security_check is False:
        return "attacker (if any) has no hp attribute, thus, it is not a Pokémon"
        # Error message to detect if a Pokémon is being used as an attacker.
    if move.category == 'special':
        damage = ((2 * 50 / 5 + 2) * move.base_power * (attacker.spatk / target.spdif) / 50 + 2) * crit_hit(move) * stab(move, attacker) * super_effective(move, target) * round(random.uniform(0.85, 1), 2)
        damage = round(damage)
        return damage
    elif move.category == 'physical':
        damage = ((2 * 50 / 5 + 2) * move.base_power * (attacker.atk / target.dif) / 50 + 2) * crit_hit(move) * stab(move, attacker) * super_effective(move, target) * round(random.uniform(0.85, 1), 2)
        damage = round(damage)
        return damage
    elif move.category == 'status':
        return 0


def accuaracy_check(move):
    """In the videogames, all moves have accuaracy and some of them can fail.
    there are also moves and abilities that can affect how likely it is
    that a Pokémon lands a certain move. In this simulation,
    the only move that can fail is Air Slash, but adding this function will help
    in case the game is updated or expanded."""
    security_check = hasattr(move, 'acc')
    if security_check is False:
        return "error: move selected does not have attribute 'acc'(accuaracy)"
    if random.randint(1, 100) <= move.acc:
        return True
    else:
        return 'the move failed!'


def move_effect(attacker, move, target):
    """Identify and apply the effect of the Pokémon moves used in battle.

    move_effect will take the move ID as its main parameter to identify a move's
    effect. To apply the effect it will need the attributes of the move's user
    or the target, as well as the effect_chance attribute, which defines how
    often an effect is succesfull.
    """
    if hasattr(move, 'effect_id') == False:
        return "Error: move selected does not have the attribute 'effect_id'"
    elif move.effect_id == 'na':
        exit
    elif move.effect_id == 'recoil':
        attacker.hp = round(attacker.hp - attacker.hp * move.effect_qty)
        dramatic_effect(f"{attacker.name} has received recoil damage! ❤️‍🩹")
        dramatic_effect(f'{attacker.name} now has 💚{attacker.hp} hp left.')
    elif move.effect_id == 'bellydrum':
        attacker.hp = round(attacker.hp - attacker.og_hp * 0.5)
        attacker.atk = round(attacker.atk * move.effect_qty)
        dramatic_effect(f"{attacker.name} lost HALF of its hp!")
        dramatic_effect(f"{attacker.name}'s attack raised to its maximum ✊🆙")
    elif move.effect_id == 'all':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
            attacker.atk = round(attacker.atk * move.effect_qty)
            attacker.dif = round(attacker.dif * move.effect_qty)
            attacker.spd = round(attacker.spd * move.effect_qty)
            attacker.spatk = round(attacker.spatk * move.effect_qty)
            attacker.spdif = round(attacker.spdif * move.effect_qty)
            dramatic_effect(f"All of {attacker.name}'s stats increased")
    elif move.effect_id == 'power':
        move.base_power = move.base_power * move.effect_qty
        if move.effect_qty < 1:
            dramatic_effect("The move's power fell!")
        else:
            dramatic_effect("The move's power has rose!")
    elif move.effect_id == 'atk':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
            attacker.atk = round(attacker.atk * move.effect_qty)
            if move.effect_qty < 1:
                dramatic_effect(f"{attacker.name}'s attack fell!")
            else:
                dramatic_effect(f"{attacker.name}'s attack rose!")
    elif move.effect_id == 'spd':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
            attacker.spd = round(attacker.spd * move.effect_qty)
            if move.effect_qty < 1:
                dramatic_effect(f"{attacker.name}'s speed fell!")
            else:
                dramatic_effect(f"{attacker.name}'s speed rose!")
    elif move.effect_id == 'def':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
            attacker.dif = round(attacker.dif * move.effect_qty)
            if move.effect_qty < 1:
                dramatic_effect(f"{attacker.name}'s defence fell!")
            else:
                dramatic_effect(f"{attacker.name}'s defence rose!")
    elif move.effect_id == 'spatk':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
            attacker.spatk = round(attacker.spatk * move.effect_qty)
            if move.effect_qty < 1:
                dramatic_effect(f"{attacker.name}'s special attack fell!")
            else:
                dramatic_effect(f"{attacker.name}'s special attack rose!")
    elif move.effect_id == 'spdef':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
            attacker.spdif = round(attacker.spdif * move.effect_qty)
            if move.effect_qty < 1:
                dramatic_effect(f"{attacker.name}'s special defence fell!")
            else:
                dramatic_effect(f"{attacker.name}'s special defence rose!")
    elif move.effect_id == 'defs':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
           attacker.dif = round(attacker.dif * move.effect_qty)
           attacker.spdif = attacker.spdif * move.effect_qty
           if move.effect_qty < 1:
                dramatic_effect(f"{attacker.name}'s defences rose!")
           else:
                dramatic_effect(f"{attacker.name}'s defences fell!")
    elif move.effect_id == 'heal':
        if attacker.hp < (attacker.og_hp * 0.5):
            attacker.hp = round(attacker.hp + attacker.og_hp * move.effect_qty)
            dramatic_effect(f"{attacker.name} regained health!")
            dramatic_effect(f"{attacker.name}'s hp is now 💚{attacker.hp}")
        elif attacker.hp >= attacker.og_hp:
            dramatic_effect(f"{attacker.name}'s is at full health!")
        else:
            attacker.hp = round(attacker.og_hp)
            dramatic_effect(f"{attacker.name} regained health, It's now fully healed!")
    elif move.effect_id == 'curs':
        attacker.atk = round(attacker.atk * 1.5)
        attacker.dif = round(attacker.dif * 1.5)
        attacker.spd = round(attacker.spd * 0.66)
        dramatic_effect(f"{attacker.name} lowered its speed to gain attack and defence!")
# Effects of moves that change the foe's stats
    elif move.effect_id == 'opp_def':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
           target.dif = round(target.dif * move.effect_qty)
           if move.effect_qty < 1:
                dramatic_effect(f"Foe {target.name}'s defence fell!")
           else:
                dramatic_effect(f"Foe {target.name}'s defence rose!")
    elif move.effect_id == 'opp_atk':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
           target.atk = round(target.atk * move.effect_qty)
           if move.effect_qty < 1:
                dramatic_effect(f"Foe {target.name}'s attack fell!")
           else:
                dramatic_effect(f"Foe {target.name}'s attack rose!")
    elif move.effect_id == 'opp_spdef':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
           target.spdif = round(target.spdif * move.effect_qty)
           if move.effect_qty < 1:
                dramatic_effect(f"Foe {target.name}'s special defence fell!")
           else:
                dramatic_effect(f"Foe {target.name}'s special defence rose!")
    elif move.effect_id == 'opp_spatk':
        chance = random.randint(1, 100)
        if chance <= move.effect_chance:
           target.spatk = round(target.spatk * move.effect_qty)
           if move.effect_qty < 1:
                dramatic_effect(f"Foe {target.name}'s special attack fell!")
           else:
                dramatic_effect(f"Foe {target.name}'s special attack rose!")

def hit_order(faster_pkmn, slower_pkmn, dmg_fast, dmg_slow, move_fast, move_slow, trainer_fast, trainer_slow):
    dramatic_effect(f"{trainer_fast}'s {faster_pkmn.name} used {move_fast.name}💥")
    time.sleep(1.5)
    is_effective = super_effective(move_fast, slower_pkmn)
    if is_effective > 1 and dmg_fast > 0:
        dramatic_effect("It's super effective!💥💥")
        time.sleep(1.5)
    slower_pkmn.hp = slower_pkmn.hp - dmg_fast
    move_effect(faster_pkmn, move_fast, slower_pkmn)
    
    if slower_pkmn.hp < 1:
        dramatic_effect(f"{slower_pkmn.name} fainted!😵‍💫")
        return 2
    elif faster_pkmn.hp < 1:
        dramatic_effect(f"{faster_pkmn.name} fainted! 😵‍💫")
        return 1
    else:
        dramatic_effect(f'{slower_pkmn.name} has 💚{slower_pkmn.hp} left')
        dramatic_effect(f"{trainer_slow}'s {slower_pkmn.name} used {move_slow.name}💥")
        time.sleep(1.5)
        is_effective = super_effective(move_slow, faster_pkmn)
        if is_effective > 1 and dmg_slow > 0:
            dramatic_effect("It's super effective!💥💥")
            time.sleep(1.5)
        faster_pkmn.hp = faster_pkmn.hp - dmg_slow
        move_effect(slower_pkmn, move_slow, faster_pkmn)

    if faster_pkmn.hp < 1:
        dramatic_effect(f"{faster_pkmn.name} fainted! 😵‍💫")
        return 1
    elif slower_pkmn.hp < 1:
        dramatic_effect(f"{slower_pkmn.name} fainted!😵‍💫")
        return 2
    else:
        dramatic_effect(f'{faster_pkmn.name} has 💚{faster_pkmn.hp} left')
    return 0

#Main
