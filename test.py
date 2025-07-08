# imports
from Pokédex import *
import sys
import time
import random
#functions

swampert1.original_stats()
def dramatic_effect(txt):
    """Type characters of a given string one by one.

    It uses a loop and functions imported from sys to print characters
    in a given string, one by one, while also adding spacing at the end.
    """
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print('\n')


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
        attacker.atk = round(attacker.atk * move.effect_qtt)
        dramatic_effect(f"{attacker} lost HALF of its hp!")
        dramatic_effect(f"{attacker}'s attack raised to its maximum ✊🆙")
    elif move.effect_id == 'all':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
            attacker.atk = round(attacker.atk * move.effect_qty)
            attacker.dif = round(attacker.dif * move.effect_qty)
            attacker.spd = round(attacker.spd * move.effect_qty)
            attacker.spatk = round(attacker.spatk * move.effect_qty)
            attacker.spdif = round(attacker.spdif * move.effect_qty)
            dramatic_effect(f"All of {attacker.name}'s stats increased")
    elif move.effect_id == 'power':
        move.base_power = move.base_power * move.effect_qty
        if move.effect.qty < 1:
            dramatic_effect("The move's power fell!")
        else:
            dramatic_effect("The move's power has rose!")
    elif move.effect_id == 'atk':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
            attacker.atk = attacker.atk * move.efffect_qty
            if move.effect.qty < 1:
                dramatic_effect(f"{attacker.name}'s attack fell!")
            else:
                dramatic_effect(f"{attacker.name}'s attack rose!")
    elif move.effect_id == 'spd':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
            attacker.spd = attacker.spd * move.efffect_qty
            if move.effect.qty < 1:
                dramatic_effect(f"{attacker.name}'s speed fell!")
            else:
                dramatic_effect(f"{attacker.name}'s speed rose!")
    elif move.effect_id == 'def':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
            attacker.dif = attacker.dif * move.efffect_qty
            if move.effect.qty < 1:
                dramatic_effect(f"{attacker.name}'s defence fell!")
            else:
                dramatic_effect(f"{attacker.name}'s defence rose!")
    elif move.effect_id == 'spatk':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
            attacker.spatk = attacker.spatk * move.efffect_qty
            if move.effect.qty < 1:
                dramatic_effect(f"{attacker.name}'s special attack fell!")
            else:
                dramatic_effect(f"{attacker.name}'s special attack rose!")
    elif move.effect_id == 'spdef':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
            attacker.spdif = attacker.spdif * move.efffect_qty
            if move.effect.qty < 1:
                dramatic_effect(f"{attacker.name}'s special defence fell!")
            else:
                dramatic_effect(f"{attacker.name}'s special defence rose!")
    elif move.effect_id == 'defs':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
           attacker.dif = attacker.dif * move.efffect_qty
           attacker.spdif = attacker.spdif * move.efffect_qty
           if move.effect.qty < 1:
                dramatic_effect(f"{attacker.name}'s defences rose!")
           else:
                dramatic_effect(f"{attacker.name}'s defences fell!")
    elif move.effect_id == 'heal':
        if attacker.hp < (attacker.og_hp * 0.5):
            attacker.hp = attacker.hp + attacker.og_hp * move.effect_qty
            dramatic_effect(f"{attacker.name} regained health!")
            dramatic_effect(f"{attacker.name}'s hp is now 💚{attacker.hp}")
        if attacker.hp >= attacker.og_hp:
            dramatic_effect(f"{attacker.name}'s is at full health!")
        else:
            attacker.hp = attacker.og_hp
            dramatic_effect(f"{attacker.name} regained health, It's now fully healed!")
    elif move.effect_id == 'curs':
        attacker.atk = attacker.atk * 1.5
        attacker.dif = attacker.dif * 1.5
        attacker.spd = attacker.spd * 0.66
        dramatic_effect(f"{attacker.name} lowered its speed to gain attack and defence!")
# Effects of moves that change the foe's stats
    elif move.effect_id == 'opp_def':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
           target.dif = target.dif * move.efffect_qty
           if move.effect.qty < 1:
                dramatic_effect(f"Foe {target.name}'s defence fell!")
           else:
                dramatic_effect(f"Foe {target.name}'s defence rose!")
    elif move.effect_id == 'opp_atk':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
           target.atk = target.atk * move.efffect_qty
           if move.effect.qty < 1:
                dramatic_effect(f"Foe {target.name}'s attack fell!")
           else:
                dramatic_effect(f"Foe {target.name}'s attack rose!")
    elif move.effect_id == 'opp_spdef':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
           target.spdif = target.spdif * move.efffect_qty
           if move.effect.qty < 1:
                dramatic_effect(f"Foe {target.name}'s special defence fell!")
           else:
                dramatic_effect(f"Foe {target.name}'s special defence rose!")
    elif move.effect_id == 'opp_spatk':
        chance = random.randit(1, 100)
        if chance <= move.effect_chance:
           target.spatk = target.spatk * move.efffect_qty
           if move.effect.qty < 1:
                dramatic_effect(f"Foe {target.name}'s special attack fell!")
           else:
                dramatic_effect(f"Foe {target.name}'s special attack rose!")


#Main
print(swampert1.og_hp)

#swampert1.hp = swampert1.hp * 0.33
#move_effect(swampert1, life_dew, decidueye1)