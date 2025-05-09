#This is the file for the Pokémon Charizard, a playable character in this game.
#I will be adding all the necesary data about its moves, statistics, etc.

#Imports
#Functions
#Main code
class Pokémon:
    def __init__(self, name, atk, dif, spd, spatk, spadif, hp, type1, type2):
        self.name = name
        self.atk = atk
        self.dif = dif
        self.spd = spd
        self.spatk = spatk
        self.spadif = spadif
        self.hp = hp
        self.type1 = type1
        self.type2 = type2

Charizard = Pokémon('charizard', 107, 101, 123, 132, 108, 156, 'fire', 'flying')

class move:
    def __init__(self, move_name, base_power, effect, effect_chance, acc, type, crit_rate, category):
        self.move_name = move_name
        self.base_power = base_power
        self.effect = effect
        self.acc = acc
        self.type = type
        self.crit_rate = crit_rate
        self.category = category
        self.effect_chance = effect_chance
    
flamethrower = move('flamethrower', 90, False, False, 100, 'fire', 417, 'special')
solar_beam = move('solar beam', 120, True, 100, 100, 'grass', 417, 'special')
air_slash = ('air slash', 75, True, 30, 95, 'flying', 417, 'special')

class moveset:
    def __init__(self, move1, move2, move3, move4):
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

toolbox_charizard = moveset('flamethrower', 'solar beam', 'air slash', 'ancient power')