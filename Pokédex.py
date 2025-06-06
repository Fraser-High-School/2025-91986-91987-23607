#This is the file for the Pokémon, the playable characters in this game.
#I will be adding all the necesary data about their moves, statistics, etc.
#Imports
#Main code
class Pokémon: #This class defines all the data about the Pokémon exept for its moves. It includes stats and typing
    def __init__(self, name, atk, dif, spd, spatk, spdif, hp, type1, type2):
        self.name = name
        self.atk = atk
        self.dif = dif
        self.spd = spd
        self.spatk = spatk
        self.spdif = spdif
        self.hp = hp
        self.type1 = type1
        self.type2 = type2

charizard1 = Pokémon('charizard', 107, 101, 123, 132, 108, 156, 'fire', 'flying')
charizard2 = Pokémon('charizard', 107, 101, 123, 132, 108, 156, 'fire', 'flying')

decidueye1 = Pokémon('decidueye', 143, 111, 91, 126, 126, 174, 'grass', 'fighting')
decidueye2 = Pokémon('decidueye', 143, 111, 91, 126, 126, 174, 'grass', 'fighting')

class move: #This class defines all the characteristics of a move, like base power, name, accuaracy, etc. Specific effects of each move will be coded separately.
    def __init__(self, move_name, base_power, effect, effect_chance, acc, ptype, crit_rate, category):
        self.move_name = move_name
        self.base_power = base_power
        self.effect = effect
        self.acc = acc
        self.ptype = ptype
        self.crit_rate = crit_rate #4.17% is the base critical hit chance of most moves, that's why most moves will have this value set to 417
        self.category = category
        self.effect_chance = effect_chance

#Toolbox Charizard moves:    
flamethrower = move('flamethrower', 90, False, 0, 100, 'fire', 417, 'special')
solar_beam = move('solar beam', 120, True, 100, 100, 'grass', 417, 'special')
air_slash = move('air slash', 75, True, 30, 95, 'flying', 417, 'special')
ancient_power = move('ancient power', 60, True, 10, 100, 'rock', 417, 'special')

#Belly drum Charizard moves:
belly_drum = move('belly drum', 0, True, 100, 100, 'normal', 0, 'status')
flare_blitz = move('flare blitz', 120, True, 100, 100, 'fire', 417, 'physical')
acrobatics = move('acrobatics', 110, False, 0, 100, 'flying', 417, "physical")
metal_claw = move('metal claw', 50, True, 10, 95, 'steel', 417, 'physical')

#List of the movesets
toolbox_charizard = ['flamethrower', 'solar beam', 'air slash', 'ancient power']
bellydrum_charizard = ['belly drum', 'flare blitz', 'acrobatics', 'metal claw']