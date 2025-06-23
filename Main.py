#Title: Pokémon Battle Pyhon Simulator
#Author: Ezequiel Ordo;ez
#Version number: 0.1
"""Desctription: A Pokémon battle simulator coded in Python. 
    In this videogame you will be able to challenge your friends to a Pokémon battle using 3 out of 4 Pokémon,
    each Pokémon has 2 movesets of 4 moves each.
    This program tries to replicate the battle system of Pokémon Scarlet and Violet,
    thus it was made pof users with prior experience with Pokémon videogames"""
#Imports
import time
import sys
from Pokédex import *
#Lists, dictionaries, and predefined variables
taken = []
decidueye_movesets = ['1', 'Swords Dance + Trailblaze', '2', 'Triple Arrows + Leaf Blade']
charizard_movesets = ['1', 'Special Attacker Toolbox', '2', 'Belly Drum']
swampert_movesets = ['1', 'Curse', '2', 'Specially Defensive']
togekiss_movesets = ['1', 'Special Attacker Toolbox', '2', 'Physical Tank']
playable_pkmn = ['1. Charizard 🦎🐦‍🔥', '2. Hisuian Decidueye 🍃🦉', '3. Swampert 🦎💧', '4. Toggekiss 🪽✨']
p1_active_pokémon = ''
p1_activepokémon_moveset = '' 
#Functions
def p(strin): #This function makes it shorter to use "print", saving me valuable time.
    print(f'{strin} \n')
    
def dramatic_effect(txt):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print('\n')
        #dramatic_effect uses a loop to type the characters in a string 1 by 1, making the program more visually appealing.

def no_blank_fields_pls (field):
    while field == '' or field.isalpha() == False:
        print("Please, only introduce words in this field.")
        time.sleep(0.5)
        #This function prevents the user from typing letters or leaving blank fields when they are asked something.
#Main code
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
player2_name = input('Introduce the name of player 2: ')
dramatic_effect(f'{player1_name}, select your first Pokémon:')
for name in playable_pkmn:
    dramatic_effect(name)
pkmn1_selected = False
while pkmn1_selected == False:
    dramatic_effect("Enter the name of the Pokémon you want to choose or write 'info <name of the Pokémon>' to know more about a certain Pokémon. ")
    pkmn_choice = input('')
    pkmn_choice = pkmn_choice.lower()
    time.sleep(1)
    if pkmn_choice == 'info decidueye' or pkmn_choice == 'info hisuian decidueye':
        """This section is specially important as there is no graphic user interface.
        A brief description with emojis will help the user to visualise the Pokemon they are about to choose"""
        dramatic_effect("Decidueye, #724 'Arrow Quill Pokémon' ✊🍂")
        dramatic_effect("Decidueye uses Triple Arrows to decrease the opponent's defense, then attacks with powerful physical moves. ")
        time.sleep(1)
    elif pkmn_choice == 'info charizard':
        dramatic_effect("Charizard, #006, 'Flame Pokémon' 🔥🐲")
        dramatic_effect("Charizard has a move for every situation. Find the right one to melt your oponent with super effective attacks.")
        time.sleep(1)
    elif pkmn_choice == 'info swampert':
        dramatic_effect("Swampert, #260, 'Mud Fish Pokémon'🐸🌊")
        dramatic_effect("Using Curse to increase its physical stats, Swampert can resist and deliver hard hits.")
        time.sleep(1)
    elif pkmn_choice == 'info togekiss':
        dramatic_effect("Togekiss, #468, 'Jubelee Pokémon' 🧚‍♀️🕊️")
        dramatic_effect("Togekiss can heal itself with Life dew while still doing great damage thanks to its high special attack.")
        time.sleep(1)
    elif pkmn_choice == 'decidueye' or pkmn_choice == 'hisuian decidueye' or pkmn_choice == '2': 
        if decidueye1 in taken:
            dramatic_effect('Sorry, that Pokemon is already taken, please use a different one')
            time.sleep(1)
            break #??
        p1_pkmn_1 = 'decidueye'
        taken.append(decidueye1)
        p1_active_pokémon = decidueye1
        dramatic_effect('Choose a moveset')
        """Here is the part in which the user gets to choose the moveset of their Pokemon.
        I decided not to include a full description of the movesets as I think randomness can make the game more amusing
        and there is a brief explanation of the Pokemon's capacities above"""
        time.sleep(1.5)
        for movset in decidueye_movesets:
            p(movset)
            time.sleep(1)
        time.sleep(0.5)
        moveset_choice = input('')
        while moveset_choice not in decidueye_movesets:
            dramatic_effect('Sorry, but I did not understand your comand, please try again ')
            moveset_choice = input('')
        if moveset_choice == '2' or moveset_choice == 'Triple Arrows + Leaf Blade':  
            dramatic_effect(f"Congrats {player1_name}, You rented 'Triple Arrows Hisuian Decidueye' successfully.")
            pkmn1_selected = True
            #A list containing the moves is assigned to the Pokémon
            p1_active_pokémon.moves = triplearrows_decidueye
            break
        elif moveset_choice == '1' or moveset_choice == 'Swords Dance + Trailblaze':
            dramatic_effect(f"Congrats {player1_name}, You rented 'Swords Dance Hisuian Decidueye' successfully.")
            pkmn1_selected = True
            p1_active_pokémon.moves = swordsdance_decidueye
            break

    elif pkmn_choice == 'charizard':
        p1_pkmn_1 = charizard1
        taken.append(charizard1)
        p1_active_pokémon = charizard1
        dramatic_effect('Choose a moveset')
        time.sleep(1.5)
        for movset in charizard_movesets:
            p(movset)
            time.sleep(1)
        time.sleep(0.5)
        moveset_choice = input('')
        moveset_choice = moveset_choice.lower()
        if moveset_choice == '2' or moveset_choice == 'belly drum':
            dramatic_effect(f"Congrats {player1_name}, You rented 'Belly Drum Charizard' successfully.")
            pkmn1_selected = True
            p1_active_pokémon.moves = bellydrum_charizard

            break
        elif moveset_choice == '1' or moveset_choice == 'special attacker toolbox':
            dramatic_effect("Congrats Trainer 1, You rented 'Toolbox Charizard' successfully.")
            pkmn1_selected = True
            p1_active_pokémon.moves = toolbox_charizard
            break
        while moveset_choice not in charizard_movesets:
            dramatic_effect('Sorry, but I did not understand your comand, please try again ')
            moveset_choice = input('')

    elif pkmn_choice == 'swampert':
        p1_pkmn_1 = swampert1
        taken.append(swampert1)
        p1_active_pokémon = swampert1
        dramatic_effect('Choose a moveset')
        time.sleep(1.5)
        for movset in swampert_movesets:
            p(movset)
            time.sleep(1)
        time.sleep(0.5)
        moveset_choice = input('')
        moveset_choice = moveset_choice.lower()
        if moveset_choice == '2' or moveset_choice == 'specially defensive':
            dramatic_effect(f"Congrats {player1_name}, You rented 'Specially Defensive Swampert' successfully.")
            pkmn1_selected = True
            p1_active_pokémon.moves = defensive_swampert
            break
        elif moveset_choice == '1' or moveset_choice == 'curse':
            dramatic_effect(f"Congrats {player1_name}, You rented 'Curse Swampert' successfully.")
            pkmn1_selected = True
            p1_active_pokémon.moves = curse_swampert
            break
        while moveset_choice not in swampert_movesets:
            dramatic_effect('Sorry, but I did not understand your comand, please try again ')
            moveset_choice = input('')

    elif pkmn_choice == 'togekiss':
        p1_pkmn_1 = togekiss1
        taken.append(togekiss1)
        p1_active_pokémon = togekiss1
        dramatic_effect('Choose a moveset')
        time.sleep(1.5)
        for movset in togekiss_movesets:
            p(movset)
            time.sleep(1)
        time.sleep(0.5)
        moveset_choice = input('')
        moveset_choice = moveset_choice.lower()
        if moveset_choice == '2' or moveset_choice == 'physical tank':
            dramatic_effect(f"Congrats {player1_name}, You rented 'Physical Tank Togekiss' successfully.")
            pkmn1_selected = True
            p1_active_pokémon.moves = tank_togekiss
            break
        elif moveset_choice == '1' or moveset_choice == 'curse':
            dramatic_effect(f"Congrats {player1_name}, You rented 'Toolbox Togekiss' successfully.")
            pkmn1_selected = True
            p1_active_pokémon.moves = toolbox_togekiss
            break
        while moveset_choice not in togekiss_movesets:
            dramatic_effect('Sorry, but I did not understand your comand, please try again ')
            moveset_choice = input('')
    else:
        dramatic_effect('Sorry, but I did not understand your comand, please try again')
        time.sleep(1)
#import Battle!