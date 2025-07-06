# imports
from Pokédex import *
import sys
import time
#functions


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
        exit
    elif move.effect_id == 'bellydrum':
        attacker.hp = round(attacker.hp * 0.5)
        attacker.atk = round(attacker.atk * move.effect_qtt)
        dramatic_effect(f"{attacker} lost HALF of its hp!")
        dramatic_effect(f"{attacker}'s attack raised to its maximum ✊🆙")
    elif move.effect_id == 'all+':
        #use random here
        attacker.atk = round(attacker.atk * move.effect_qty)
        attacker.dif = round(attacker.dif * move.effect_qty)
        attacker.spd = round(attacker.spd * move.effect_qty)
        attacker.spatk = round(attacker.spatk * move.effect_qty)
        attacker.spdif = round(attacker.spdif * move.effect_qty)
        dramatic_effect(f"All of {attacker.name}'s stats increased")
#Main
move_effect(charizard1, flare_blitz, decidueye1)