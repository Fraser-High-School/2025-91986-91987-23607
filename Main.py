# Title: Pokémon Battle Pyhon Simulator
# Author: Ezequiel Ordoñez
# Version number: 1.0
"""Desctription: A Pokémon battle simulator coded in Python.

In this videogame you will be able to challenge your friends
to a Pokémon battle using 3 out of 4 Pokémon.
Each Pokémon has 2 movesets of 4 moves each.
This program tries to replicate the battle system of Pokémon Scarlet and
Pokémon Violet, thus it was made for users with prior experience
with Pokémon videogames.
"""
# Imports
import time
import sys
from Pokédex import *
# Lists, dictionaries, and predefined variables
taken = []
p1_pokémon_team = []
p2_pokémon_team = []
decidueye_movesets = ['1', 'Swords Dance + Trailblaze',
                      '2', 'Triple Arrows + Leaf Blade']
charizard_movesets = ['1', 'Special Attacker Toolbox', '2', 'Belly Drum']
swampert_movesets = ['1', 'Curse', '2', 'Specially Defensive']
togekiss_movesets = ['1', 'Special Attacker Toolbox', '2', 'Physical Tank']
playable_pkmn = ['1. Charizard 🦎🐦‍🔥', '2. Hisuian Decidueye 🍃🦉',
                 '3. Swampert 🦎💧', '4. Toggekiss 🪽✨']
# Functions


def p(strin):
    r"""Make it shorter to use 'print', and add spacing after the string.

    I later added '\n' to the end of the string, making this function sligthly
    different from 'print', and also saving space and time later on,
    when spacing is neccesary.
    """
    print(f'{strin}\n')


def dramatic_effect(txt):
    """Type characters of a given string one by one.

    It uses a loop and functions imported from sys to print characters
    in a given string, one by one, while also adding spacing at the end.
    """
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    print('\n')


# Main code
dramatic_effect('Welcome to the')
time.sleep(0.5)
p('⭐Pokémon⭐')
time.sleep(0.5)
p('⭐Battle⭐')
time.sleep(0.5)
p('⭐Python⭐')
time.sleep(0.5)
dramatic_effect('⭐Simulator!!⭐')
time.sleep(1.5)
start = input("Press 'ENTER' to start ")
time.sleep(0.5)
player1_name = input('Introduce the name of player 1: ')
time.sleep(1.5)
player2_name = input('Introduce the name of player 2: ')

for pkmn in range(3):
    dramatic_effect(f'{player1_name}, select your Pokémon {pkmn + 1}:')
    for name in playable_pkmn:
        dramatic_effect(name)
    pkmn_selected = False
    while pkmn_selected is False:
        dramatic_effect("Enter the name of the Pokémon you want to choose or write "
                        "'info <name of the Pokémon>' to know more about a certain Pokémon. ")
        pkmn_choice = input('')
        pkmn_choice = pkmn_choice.lower()
        time.sleep(1)
        if pkmn_choice == 'info decidueye' or pkmn_choice == 'info hisuian decidueye':
            """This section is specially important as there is no graphic
            user interface. A brief description with emojis will help the user
            to visualise the Pokémon they are about to choose"""
            dramatic_effect("Decidueye, # 724 'Arrow Quill Pokémon' ✊🍂")
            dramatic_effect("Decidueye uses Triple Arrows to decrease the opponent's"
                            " defense, then attacks with powerful physical moves. ")
            time.sleep(1)
        elif pkmn_choice == 'info charizard':
            dramatic_effect("Charizard, # 006, 'Flame Pokémon' 🔥🐲")
            dramatic_effect("Charizard has a move for every situation. Find the right"
                            " one to melt your oponent with super effective attacks.")
            time.sleep(1)
        elif pkmn_choice == 'info swampert':
            dramatic_effect("Swampert, # 260, 'Mud Fish Pokémon'🐸🌊")
            dramatic_effect("Using Curse to increase its physical stats, "
                            "Swampert can resist and deliver hard hits.")
            time.sleep(1)
        elif pkmn_choice == 'info togekiss':
            dramatic_effect("Togekiss, # 468, 'Jubelee Pokémon' 🧚‍♀️🕊️")
            dramatic_effect("Togekiss can heal itself with Life dew while still "
                            "doing great damage thanks to its high special attack.")
            time.sleep(1)
        elif pkmn_choice == 'decidueye' or pkmn_choice == 'hisuian decidueye' or pkmn_choice == '2':
            if decidueye1 in taken:
                dramatic_effect('You have selected that Pokémon already,'
                                ' please choose a different one')
                time.sleep(1)
                pkmn_selected = False
            else:
                taken.append(decidueye1)
                p1_pokémon_team.append(decidueye1)
                dramatic_effect('Choose a moveset')
                """Here is the part in which the user chooses their Pokémon's moveset.
                I decided not to include a full description of the movesets
                as I think choosing blindly can make the game more amusing
                and there is a brief explanation of the Pokémon's capacities above"""
                time.sleep(1.5)
                for movset in decidueye_movesets:
                    p(movset)
                    time.sleep(1)
                time.sleep(0.5)
                moveset_choice = input('')
                while moveset_choice not in decidueye_movesets:
                    dramatic_effect('Sorry, but I did not understand your comand,'
                                    ' please try again')
                    moveset_choice = input('')
                if moveset_choice == '2' or moveset_choice == 'Triple Arrows + Leaf Blade':
                    dramatic_effect(f"Congrats {player1_name}, You rented "
                                    "'Triple Arrows Hisuian Decidueye' successfully.")
                    pkmn_selected = True
                    # A list containing the moves is assigned to the Pokémon
                    p1_pokémon_team[pkmn].moves = triplearrows_decidueye
                    break
                elif moveset_choice == '1' or moveset_choice == 'Swords Dance + Trailblaze':
                    dramatic_effect(f"Congrats {player1_name}, You rented "
                                    "'Swords Dance Hisuian Decidueye' successfully.")
                    pkmn_selected = True
                    p1_pokémon_team[pkmn].moves = swordsdance_decidueye
                    break

        elif pkmn_choice == 'charizard' or pkmn_choice == '1':
            if charizard1 in taken:
                dramatic_effect('You have selected that Pokémon already,'
                                ' please choose a different one')
                time.sleep(1)
                pkmn_selected = False
            else:
                taken.append(charizard1)
                p1_pokémon_team.append(charizard1)
                dramatic_effect('Choose a moveset')
                time.sleep(1.5)
                for movset in charizard_movesets:
                    p(movset)
                    time.sleep(1)
                time.sleep(0.5)
                moveset_choice = input('')
                moveset_choice = moveset_choice.lower()
                if moveset_choice == '2' or moveset_choice == 'belly drum':
                    dramatic_effect(f"Congrats {player1_name}, You rented "
                                    "'Belly Drum Charizard' successfully.")
                    pkmn_selected = True
                    p1_pokémon_team[pkmn].moves = bellydrum_charizard
                    break
                elif moveset_choice == '1' or moveset_choice == 'special attacker toolbox':
                    dramatic_effect(f"Congrats {player1_name}, You rented "
                                    "'Toolbox Charizard' successfully.")
                    pkmn_selected = True
                    p1_pokémon_team[pkmn].moves = toolbox_charizard
                    break
                while moveset_choice not in charizard_movesets:
                    dramatic_effect('Sorry, but I did not understand your comand, '
                                    'please try again ')
                    moveset_choice = input('')

        elif pkmn_choice == 'swampert' or pkmn_choice == '3':
            if swampert1 in taken:
                dramatic_effect('You have selected that Pokémon already,'
                                ' please choose a different one')
                break
            taken.append(swampert1)
            p1_pokémon_team.append(swampert1)
            dramatic_effect('Choose a moveset')
            time.sleep(1.5)
            for movset in swampert_movesets:
                p(movset)
                time.sleep(1)
            time.sleep(0.5)
            moveset_choice = input('')
            moveset_choice = moveset_choice.lower()
            if moveset_choice == '2' or moveset_choice == 'specially defensive':
                dramatic_effect(f"Congrats {player1_name}, You rented "
                                "'Specially Defensive Swampert' successfully.")
                pkmn_selected = True
                p1_pokémon_team[pkmn].moves = defensive_swampert
                break
            elif moveset_choice == '1' or moveset_choice == 'curse':
                dramatic_effect(f"Congrats {player1_name}, You rented "
                                "'Curse Swampert' successfully.")
                pkmn_selected = True
                p1_pokémon_team[pkmn].moves = curse_swampert
                break
            while moveset_choice not in swampert_movesets:
                dramatic_effect('Sorry, but I did not understand your comand,'
                                ' please try again ')
                moveset_choice = input('')

        elif pkmn_choice == 'togekiss' or pkmn_choice == '4':
            if togekiss1 in taken:
                dramatic_effect('You have selected that Pokémon already,'
                                ' please choose a different one')
                break
            taken.append(togekiss1)
            p1_pokémon_team.append(togekiss1)
            dramatic_effect('Choose a moveset')
            time.sleep(1.5)
            for movset in togekiss_movesets:
                p(movset)
                time.sleep(1)
            time.sleep(0.5)
            moveset_choice = input('')
            moveset_choice = moveset_choice.lower()
            if moveset_choice == '2' or moveset_choice == 'physical tank':
                dramatic_effect(f"Congrats {player1_name}, You rented "
                                "'Physical Tank Togekiss' successfully.")
                pkmn_selected = True
                p1_pokémon_team[pkmn].moves = tank_togekiss
                break
            elif moveset_choice == '1' or moveset_choice == 'curse':
                dramatic_effect(f"Congrats {player1_name}, You rented"
                                " 'Toolbox Togekiss' successfully.")
                pkmn_selected = True
                p1_pokémon_team[pkmn].moves = toolbox_togekiss
                break
            while moveset_choice not in togekiss_movesets:
                dramatic_effect(
                    'Sorry, but I did not understand your comand, please try again ')
                moveset_choice = input('')
        else:
            dramatic_effect("Sorry, but I did not understand your comand. "
                            "Answer with the name of the Pokémon or "
                            "their number (eg. 1, 3) on the list")
            time.sleep(1)

dramatic_effect(f"{player1_name}, here is your team:")
for pkmn in p1_pokémon_team:
    print(pkmn.name)
    for move in pkmn.moves:
        p(move.name)

# Player 2 chooses their Pokémon
for pkmn in range(3):
    dramatic_effect(f'{player2_name}, select your Pokémon {pkmn + 1}:')
    for name in playable_pkmn:
        dramatic_effect(name)
    pkmn_selected = False
    while pkmn_selected is False:
        dramatic_effect("Enter the name of the Pokémon you want to choose or write "
                        "'info <name of the Pokémon>' to know more about a certain Pokémon. ")
        pkmn_choice = input('')
        pkmn_choice = pkmn_choice.lower()
        time.sleep(1)
        if pkmn_choice == 'info decidueye' or pkmn_choice == 'info hisuian decidueye':
            dramatic_effect("Decidueye, # 724 'Arrow Quill Pokémon' ✊🍂")
            dramatic_effect("Decidueye uses Triple Arrows to decrease the opponent's"
                            " defense, then attacks with powerful physical moves. ")
            time.sleep(1)
        elif pkmn_choice == 'info charizard':
            dramatic_effect("Charizard, # 006, 'Flame Pokémon' 🔥🐲")
            dramatic_effect("Charizard has a move for every situation. Find the right"
                            " one to melt your oponent with super effective attacks.")
            time.sleep(1)
        elif pkmn_choice == 'info swampert':
            dramatic_effect("Swampert, # 260, 'Mud Fish Pokémon'🐸🌊")
            dramatic_effect("Using Curse to increase its physical stats, "
                            "Swampert can resist and deliver hard hits.")
            time.sleep(1)
        elif pkmn_choice == 'info togekiss':
            dramatic_effect("Togekiss, # 468, 'Jubelee Pokémon' 🧚‍♀️🕊️")
            dramatic_effect("Togekiss can heal itself with Life dew while still "
                            "doing great damage thanks to its high special attack.")
            time.sleep(1)
        elif pkmn_choice == 'decidueye' or pkmn_choice == 'hisuian decidueye' or pkmn_choice == '2':
            if decidueye2 in taken:
                dramatic_effect('You have selected that Pokémon already,'
                                ' please choose a different one')
                time.sleep(1)
                pkmn_selected = False
            else:
                taken.append(decidueye2)
                p2_pokémon_team.append(decidueye2)
                dramatic_effect('Choose a moveset')
                time.sleep(1.5)
                for movset in decidueye_movesets:
                    p(movset)
                    time.sleep(1)
                time.sleep(0.5)
                moveset_choice = input('')
                while moveset_choice not in decidueye_movesets:
                    dramatic_effect('Sorry, but I did not understand your comand,'
                                    ' please try again')
                    moveset_choice = input('')
                if moveset_choice == '2' or moveset_choice == 'Triple Arrows + Leaf Blade':
                    dramatic_effect(f"Congrats {player2_name}, You rented "
                                    "'Triple Arrows Hisuian Decidueye' successfully.")
                    pkmn_selected = True
                    p2_pokémon_team[pkmn].moves = triplearrows_decidueye
                    break
                elif moveset_choice == '1' or moveset_choice == 'Swords Dance + Trailblaze':
                    dramatic_effect(f"Congrats {player2_name}, You rented "
                                    "'Swords Dance Hisuian Decidueye' successfully.")
                    pkmn_selected = True
                    p2_pokémon_team[pkmn].moves = swordsdance_decidueye
                    break

        elif pkmn_choice == 'charizard' or pkmn_choice == '1':
            if charizard2 in taken:
                dramatic_effect('You have selected that Pokémon already,'
                                ' please choose a different one')
                time.sleep(1)
                pkmn_selected = False
            else:
                taken.append(charizard2)
                p2_pokémon_team.append(charizard2)
                dramatic_effect('Choose a moveset')
                time.sleep(1.5)
                for movset in charizard_movesets:
                    p(movset)
                    time.sleep(1)
                time.sleep(0.5)
                moveset_choice = input('')
                moveset_choice = moveset_choice.lower()
                if moveset_choice == '2' or moveset_choice == 'belly drum':
                    dramatic_effect(f"Congrats {player2_name}, You rented "
                                    "'Belly Drum Charizard' successfully.")
                    pkmn_selected = True
                    p2_pokémon_team[pkmn].moves = bellydrum_charizard
                    break
                elif moveset_choice == '1' or moveset_choice == 'special attacker toolbox':
                    dramatic_effect(f"Congrats {player2_name}, You rented "
                                    "'Toolbox Charizard' successfully.")
                    pkmn_selected = True
                    p2_pokémon_team[pkmn].moves = toolbox_charizard
                    break
                while moveset_choice not in charizard_movesets:
                    dramatic_effect('Sorry, but I did not understand your comand, '
                                    'please try again ')
                    moveset_choice = input('')

        elif pkmn_choice == 'swampert' or pkmn_choice == '3':
            if swampert2 in taken:
                dramatic_effect('You have selected that Pokémon already,'
                                ' please choose a different one')
                break
            taken.append(swampert2)
            p2_pokémon_team.append(swampert2)
            dramatic_effect('Choose a moveset')
            time.sleep(1.5)
            for movset in swampert_movesets:
                p(movset)
                time.sleep(1)
            time.sleep(0.5)
            moveset_choice = input('')
            moveset_choice = moveset_choice.lower()
            if moveset_choice == '2' or moveset_choice == 'specially defensive':
                dramatic_effect(f"Congrats {player2_name}, You rented "
                                "'Specially Defensive Swampert' successfully.")
                pkmn_selected = True
                p2_pokémon_team[pkmn].moves = defensive_swampert
                break
            elif moveset_choice == '1' or moveset_choice == 'curse':
                dramatic_effect(f"Congrats {player2_name}, You rented "
                                "'Curse Swampert' successfully.")
                pkmn_selected = True
                p2_pokémon_team[pkmn].moves = curse_swampert
                break
            while moveset_choice not in swampert_movesets:
                dramatic_effect('Sorry, but I did not understand your comand,'
                                ' please try again ')
                moveset_choice = input('')

        elif pkmn_choice == 'togekiss' or pkmn_choice == '4':
            if togekiss2 in taken:
                dramatic_effect('You have selected that Pokémon already,'
                                ' please choose a different one')
                break
            taken.append(togekiss2)
            p2_pokémon_team.append(togekiss2)
            dramatic_effect('Choose a moveset')
            time.sleep(1.5)
            for movset in togekiss_movesets:
                p(movset)
                time.sleep(1)
            time.sleep(0.5)
            moveset_choice = input('')
            moveset_choice = moveset_choice.lower()
            if moveset_choice == '2' or moveset_choice == 'physical tank':
                dramatic_effect(f"Congrats {player2_name}, You rented "
                                "'Physical Tank Togekiss' successfully.")
                pkmn_selected = True
                p2_pokémon_team[pkmn].moves = tank_togekiss
                break
            elif moveset_choice == '1' or moveset_choice == 'curse':
                dramatic_effect(f"Congrats {player2_name}, You rented"
                                " 'Toolbox Togekiss' successfully.")
                pkmn_selected = True
                p2_pokémon_team[pkmn].moves = toolbox_togekiss
                break
            while moveset_choice not in togekiss_movesets:
                dramatic_effect(
                    'Sorry, but I did not understand your comand, please try again ')
                moveset_choice = input('')
        else:
            dramatic_effect("Sorry, but I did not understand your comand. "
                            "Answer with the name of the Pokémon or "
                            "their number (eg. 1, 3) on the list")
            time.sleep(1)

dramatic_effect(f"{player2_name}, here is your team:")
for pkmn in p2_pokémon_team:
    print(pkmn.name)
    for move in pkmn.moves:
        p(move.name)

# import Battle
