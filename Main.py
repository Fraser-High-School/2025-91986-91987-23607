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