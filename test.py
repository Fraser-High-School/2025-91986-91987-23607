import sys
import time

def p(strin):
    print(f'{strin} \n')

def dramatic_effect(txt):
    for letter in txt:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print('\n')

dramatic_effect('unfg')
dramatic_effect('dasa')
