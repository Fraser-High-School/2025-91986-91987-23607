# imports
from Pokédex import *
from Main import dramatic_effect
# Lists, dictionaries and variables


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
    elif move.effect_id == 'recoil33':
        attacker.hp = round(attacker.hp * 0.33)
        dramatic_effect(f"{attacker} has received recoil damage! ❤️‍🩹")
        dramatic_effect(f'{attacker} now has 💚{attacker.hp} hp left.')
        exit
    elif move.effect_id == 'bellydrum':
        attacker.hp = round(attacker.hp * 0.5)
        attacker.atk = round(attacker.atk * 4)
        dramatic_effect(f"{attacker} lost HALF of its hp!")
        dramatic_effect(f"{attacker}'s attack raised to its maximum ✊🆙")
#Main
move_effect(charizard1, flare_blitz, decidueye1)