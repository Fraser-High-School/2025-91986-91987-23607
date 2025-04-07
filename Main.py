#Imports
import time
import sys
import random
#Functions
def p(strin):
    print(strin)
    #This function makes it shorter to use "print", saving me valuable time.
def dramatic_effect(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
#Main code
dramatic_effect('Welcome to the\n')
time.sleep(0.5)
p('⭐Pokemon⭐')
time.sleep(0.5)
p('⭐Battle⭐')
time.sleep(0.5)
p('⭐Python⭐')
time.sleep(0.5)
dramatic_effect('⭐Simulator!!⭐')