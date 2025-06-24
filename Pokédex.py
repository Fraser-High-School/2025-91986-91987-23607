#This is the file for the Pokémon, the playable characters in this game. version: 1
#I will be adding all the necesary data about their moves, statistics, etc.
#Imports
#Main code


class Pokémon:
    """This class defines all the data about the Pokémon exept for its moves. It includes stats and typing.
    other attributes present in the original material were disregaded as this adaptation will not use those attributes,
    or those attributes will be imposible to change, like abilities, nature, etc."""
    def __init__(self, name, atk, dif, spd, spatk, spdif, hp, typing, moves = ['placeholder']):
        self.name = name
        self.atk = atk
        self.dif = dif
        self.spd = spd
        self.spatk = spatk
        self.spdif = spdif
        self.hp = hp
        self.typing = typing
        self.moves = moves


"""I decided to code each Pokémon twice with 2 different names,
as both players will be able to have one at the same time,
with the same attributes, but Python does not naturally allow object clonation, 
so, if I want 2 copies of the same object, I have to code 2 separate objects and
give them the same attributes"""
#Object Charizard
charizard1 = Pokémon('charizard', 107, 101, 123, 132, 108, 156, ['fire', 'flying'])
charizard2 = Pokémon('charizard', 107, 101, 123, 132, 108, 156, ['fire', 'flying'])

#Object Decidueye
decidueye1 = Pokémon('decidueye', 143, 111, 91, 126, 126, 174, ['grass', 'fighting'])
decidueye2 = Pokémon('decidueye', 143, 111, 91, 126, 126, 174, ['grass', 'fighting'])

#Object Swampert
swampert1 = Pokémon('swampert', 141, 121, 91, 116, 121, 186, ['water', 'ground'])
swampert2 = Pokémon('swampert', 141, 121, 91, 116, 121, 186, ['water', 'ground'])

#Object Togekiss
togekiss1 = Pokémon('togekiss', 81, 126, 111, 151, 146, 171, ['fairy', 'flying'])
togekiss2 = Pokémon('togekiss', 81, 126, 111, 151, 146, 171, ['fairy', 'flying'])


class move: 
    """This class defines all the characteristics of a move, like base power, name, accuaracy, etc.
    Specific effects of each move will be coded separately. Other attributes present in the orignal material were 
    disregarded as ther will not be used for this simulation, like priority, field effects, secret 'types', etc."""
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

#Triple Arrows Decidueye moves
triple_arrows = move('triple arrows', 90, True, 50, 100, 'fighting', 1250, 'physical')
leaf_blade = move('leaf blade', 90, False, 0, 100, 'grass', 1250, 'physical')
brave_bird = move('brave bird', 120, True, 100, 100, 'flying', 417, 'physical')
steel_wing = move('steel wing', 70, True, 10, 90, 'steel', 417, 'physical')

#Swords Dance Decidueye moves
swords_dance = move('swords dance', 0, True, 100, 100, 'normal', 0, 'status')
sucker_punch = move('sucker punch', 70, True, 50, 100, 'dark', 417, 'physical')
trailblaze = move('trailblaze', 50, True, 100, 100, 'grass', 417, 'physical')
close_combat = move('close combat', 120, True, 100, 100, 'fighting', 417, 'physical')

#Curse Swampert moves
curse = move('curse', 0, True, 100, 100, 'ghost', 0, 'status')
water_pledge = move('water pledge', 80, False, 0, 100, 'water', 417, 'special')
ice_punch = move('ice punch', 75, False, 0, 100, 'ice', 417, 'physical')
earthquake = move('earthquake', 100, False, 0, 100, 'ground', 417, 'physical')

#Defensive Swampert moves
ice_beam = move('ice beam', 90, False, 0, 100, 'ice', 417, 'special')
surf = move('surf', 90, False, 0, 100, 'water', 417, 'special')
life_dew = move('life dew', 0, True, 100, 100, 'water', 0, 'status')
amnesia = move('amnesia', 0, True, 100, 100, 'psychic', 0, 'status')

#Toolbox Togekiss moves
water_pulse = move('water pulse', 60, False, 0, 100, 'water', 417, 'special')
shock_wave = move('shock wave', 60, False, 0, 100, 'electric', 417, 'special')
gust = move('gust', 40, False, 0, 100, 'flying', 417, 'special')

#Tank Togekiss moves
charm = move('charm', 0, True, 100, 100, 'fairy', 417, 'status')
shadow_ball = move('shadow ball', 80, True, 20, 100, 'ghost', 417, 'special')
magical_leaf = move('magical leaf', 60, False, 0, 100, 'grass', 417, 'special')

"""Lists of the movesets: This will be displayed when the player has to choose their move"""
#Charizard's movesets
toolbox_charizard = [flamethrower, solar_beam, air_slash, ancient_power]
bellydrum_charizard = [belly_drum, flare_blitz, acrobatics, metal_claw]
#Decidueyes movesets
triplearrows_decidueye = [triple_arrows, leaf_blade, brave_bird, steel_wing]
swordsdance_decidueye = [swords_dance, sucker_punch, trailblaze, close_combat]
#Swamperts movesets
curse_swampert = [curse, water_pledge, ice_punch, earthquake]
defensive_swampert = [ice_beam, surf, life_dew, amnesia]
#Togekisss movesets
toolbox_togekiss = [ancient_power, water_pulse, shock_wave, gust]
tank_togekiss = [charm, life_dew, shadow_ball, magical_leaf]