#Imports
import time
import sys
import random
#Functions
def p(strin):
    print(strin)
    #This function makes it shorter to use "print", saving me valuable time.
def dramatic_effect(txt):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
        #dramatic_effect uses a loop to type the characters in a string 1 by 1, making the program more visually appealing.

def no_blank_fields_pls (field):
    '''If the user does not fill a field, this function will detect it and ask them to do it'''
    while field == '' or field.isalpha() == False:
        print("Please, only introduce words in this field.")
        time.sleep(0.5)
        #This function prevents the user from typing letters or leaving blank fields when they are asked something.
#Main code
dramatic_effect('Welcome to the\n')
time.sleep(0.5)
p('⭐Pokémon⭐')
time.sleep(0.5)
p('⭐Battle⭐')
time.sleep(0.5)
p('⭐Python⭐')
time.sleep(0.5)
dramatic_effect('⭐Simulator!!⭐')
time.sleep(1)
start = input("Press 'ENTER' to start ")
time.sleep(0.5)
dramatic_effect('Select your Pokémon:\n')
dramatic_effect('Charizard 🦎🐦‍🔥\n')
dramatic_effect('Hisuian Decidueye 🍃🦉\n')
dramatic_effect('Swampert 🦎💧\n')
dramatic_effect('Toggekiss 🪽✨\n')
for n in 3:
    while True:
        p1_pkmn = input(dramatic_effect("Enter the name of the Pokémon you want to choose or write 'info <name of the Pokémon>' to know more about a certain Pokémon. "))
        p1_pkmn = p1_pkmn.lower()
        time.sleep(1)
        if p1_pkmn == 'info decidueye':
            dramatic_effect("Decidueye, #724 'Arrow Quill Pokémon'")
            dramatic_effect("Decidueye uses Triple Arrow to increase the chance of landing critical hits, then attacks with powerful physical moves.")
            time.sleep(1)
        elif p1_pkmn == 'info charizard':
            dramatic_effect("Charizard, #006, 'Flame Pokémon'")
            dramatic_effect("Charizard has a move for every situation. Find the right one to melt your oponent with super effective attacks.")
            time.sleep(1)
        elif p1_pkmn == 'info Swampert':
            dramatic_effect("Swampert, #260, 'Mud Fish Pokémon'")
            dramatic_effect("Using Curse to increase its physical stats, Swampert can resist and deliver hard hits.")
            time.sleep(1)
        elif p1_pkmn == 'info togekiss':
            dramatic_effect("Togekiss, #468, 'Jubelee Pokémon'")
            dramatic_effect("Togekiss can heal itself with Daining kiss and use Defog to bring the Pokémon's stats back to normal.")
            time.sleep(1)
        elif p1_pkmn == 'decidueye':
            p1_pkmn_1 = 'decidueye'
            p1_pkmn_1_moveset = input(dramatic_effect('Choose '))
            break
        
        else:
            dramatic_effect('Sorry, but I did not understand your comand, please try again')