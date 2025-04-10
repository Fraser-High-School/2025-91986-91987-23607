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
p1_pkmn = input(dramatic_effect("Enter the name of the Pokémon you want to choose or write 'info <name of the Pokémon>' to know more about a certain Pokémon. "))
p1_pkmn = p1_pkmn.lower()
if p1_pkmn == 'info decidueye':
    dramatic_effect('Decidueye')