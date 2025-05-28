# imports
#from playsound import playsound
from Charizard import *
# for playing note.wav file
#playsound('https://archive.org/details/pokemon-sv-ost-rip/Battle!+(Nemona).mp3')
#print('playing sound using playsound')
def stab(move, attacker):
    if any(x >= 2 for x in ((attacker).type1, (attacker)type2, (move).ptype)):
        return 1.5
    
