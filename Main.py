#Title: Pokémon Battle Python Simulator
#Author: Ezequiel Ordo;ez
#Version number: 0.1
#Desctription: A Pokémon battle simulator coded in Python. In this videogame you will be able to challenge your friends to a Pokémon battle using 3 out of 4 Pokémon, each Pokémon has 2 movesets of 4 moves each.
#Imports
import time
import sys
from Pokédex import *
#Lists and dictionaries
taken = []
decidueye_movesets = ['1', 'Swords Dance + Trailblaze', '2', 'Triple Arrows + Leaf Blade']
charizard_movesets = ['1', 'Special Attacker Toolbox', '2', 'Belly Drum']
pokémon_call ={
    
}
playable_pkmn = ['Charizard 🦎🐦‍🔥', 'Hisuian Decidueye 🍃🦉', 'Swampert 🦎💧', 'Toggekiss 🪽✨']
#Functions
def p(strin): 
    """This function makes it shorter to use "print", saving me valuable time."""
    print(f'{strin} \n')

def dramatic_effect(txt):
    """dramatic_effect uses a loop to type the characters in a string 1 by 1, making the program more visually appealing."""
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print('\n')
       

def no_blank_fields_pls (field):
    """This function prevents the user from typing letters or leaving blank fields when they are asked something."""
    while field == '' or field.isalpha() == False:
        print("Please, only introduce words in this field.")
        time.sleep(0.5)
       
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
        """This section is specially important as there is no graphic user interface.
    A brief description with emojis will help the user to visualise the Pokemon they are about to choose""""
    if pkmn_choice == 'info decidueye':
        dramatic_effect("Decidueye, #724 'Arrow Quill Pokémon'")
        dramatic_effect("Decidueye uses Triple Arrow to increase the chance of landing critical hits, then attacks with powerful physical moves.")
        time.sleep(1)
    elif pkmn_choice == 'info charizard':
        dramatic_effect("Charizard, #006, 'Flame Pokémon'")
        dramatic_effect("Charizard has a move for every situation. Find the right one to melt your oponent with super effective attacks.")
        time.sleep(1)
    elif pkmn_choice == 'info swampert':
        dramatic_effect("Swampert, #260, 'Mud Fish Pokémon'")
        dramatic_effect("Using Curse to increase its physical stats, Swampert can resist and deliver hard hits.")
        time.sleep(1)
    elif pkmn_choice == 'info togekiss':
        dramatic_effect("Togekiss, #468, 'Jubelee Pokémon'")
        dramatic_effect("Togekiss can heal itself with Daining kiss while still doing damage.")
        time.sleep(1)
    elif pkmn_choice == 'decidueye': #Here is the part in which the user gets to choose the moveset of their Pokemon.
        #I decided not to include a full description of the movesets as I think randomness can make the game more amusing, and there is a brief explanation of the Pokemon's capacities above
        if decidueye1 in taken:
            dramatic_effect('Sorry, that Pokemon is already take, please use a different one')
            time.sleep(1)
            break #??
        p1_pkmn_1 = 'decidueye'
        taken.append(decidueye1)
        pokémon_call.update{[active_pokemon : decidueye1]}
        dramatic_effect('Choose a moveset')
        time.sleep(1.5)
        for movset in decidueye_movesets:
            p(movset)
            time.sleep(1)
        time.sleep(0.5)
        p1_pkmn_1_moveset = input('')
        while p1_pkmn_1_moveset not in decidueye_movesets:
            dramatic_effect('Sorry, but I did not understand your comand, please try again ')
            p1_pkmn_1_moveset = input('')
        if p1_pkmn_1_moveset == '2' or p1_pkmn_1_moveset == 'Triple Arrows + Leaf Blade':  
            dramatic_effect(f"Congrats {player1_name}, You rented 'Triple Arrows Hisuian Decidueye' successfully.")
            pkmn1_selected = True
            pokémon_call.update{[p1_activepkmn_moveset : triplearrows_decidueye]}
            break
        elif p1_pkmn_1_moveset == '1' or p1_pkmn_1_moveset == 'Swords Dance + Trailblaze':
            dramatic_effect(f"Congrats {player1_name}, You rented 'Swords Dance Hisuian Decidueye' successfully.")
            pkmn1_selected = True
            pokémon_call.update{[p1_activepkmn_moveset : swordsdance_decidueye]}
            break

    elif pkmn_choice == 'charizard':
        p1_pkmn_1 = charizard1
        taken.append(charizard1)
        pokémon_call.update{[active_pokemon : charizard1]}
        dramatic_effect('Choose a moveset')
        time.sleep(1.5)
        for movset in charizard_movesets:
            p(movset)
            time.sleep(1)
        time.sleep(0.5)
        p1_pkmn_1_moveset = input('')
        p1_pkmn_1_moveset = p1_pkmn_1_moveset.lower()
        if p1_pkmn_1_moveset == '2' or p1_pkmn_1_moveset == 'belly drum':
            dramatic_effect("Congrats Trainer 1, You rented 'Belly Drum' successfully.")
            pkmn1_selected = True
            break
        elif p1_pkmn_1_moveset == '1' or p1_pkmn_1_moveset == 'special attacker toolbox':
            pkmn1_equals = dict(p1_pkmn1 = charizard1, p1_pkmn1_moveset = toolbox_charizard)
            dramatic_effect("Congrats Trainer 1, You rented 'Toolbox Charizard' successfully.")
            pkmn1_selected = True
            break
        while p1_pkmn_1_moveset not in charizard_movesets:
            dramatic_effect('Sorry, but I did not understand your comand, please try again ')
            p1_pkmn_1_moveset = input('')
    else:
        dramatic_effect('Sorry, but I did not understand your comand, please try again')
        time.sleep(1)
import Battle!