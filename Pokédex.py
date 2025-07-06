#This is the file for the Pokémon, the playable characters in this game. version: 1
#I will be adding all the necesary data about their moves, statistics, etc.
#Imports
#Main code


class Pokémon:
    """This class defines all the data about the Pokémon exept for its moves.
    It includes stats and typing. Other attributes present in the original
    material were disregaded as this adaptation will not use those attributes,
    or those attributes will be imposible to change, like abilities, nature, etc.
    """
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
with the same attributes, but Python does not naturally allow
object clonation, so, if I want 2 copies of the same object, I have to
code 2 separate objects and give them the same attributes
"""
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
    """This class defines all the characteristics of a move, like base power,
    name, accuaracy, etc. Specific effects of each move will be coded separately.
    Other attributes present in the orignal material were disregarded as they
    will not be used for this simulation, like priority, field effects, etc.
    """
    def __init__(self, move_name, base_power, effect_chance, acc, ptype, crit_rate, category, effect_id, effect_qty):
        self.move_name = move_name
        self.base_power = base_power
        self.acc = acc
        self.ptype = ptype
        self.crit_rate = crit_rate
        # 4.17% is the base critical hit chance of most moves,
        # that's why most moves will have this value set to 417
        self.category = category
        self.effect_chance = effect_chance
        self.effect_id = effect_id
        self.effect_qty = effect_qty


#Toolbox Charizard moves:    
flamethrower = move('flamethrower', 90, 0, 100, 'fire', 417, 'special', 'na', 0)
solar_beam = move('solar beam', 120, 100, 100, 'grass', 417, 'special', 'charge', 0)
air_slash = move('air slash', 75, 30, 95, 'flying', 417, 'special', 'na', 0)
ancient_power = move('ancient power', 60, 10, 100, 'rock', 417, 'special', 'all+', 1.5)

#Belly drum Charizard moves:
belly_drum = move('belly drum', 0, 100, 100, 'normal', 0, 'status', 'bellydrum', 4)
"""I decided to give belly_drum the effect id 'bellydrum' as no other move has
the same effect as Belly Drum in the original material. Therefore, making a
generic effect id for this effect is unnecesary. The same is true for other
moves with effect IDs that resemble their names.
"""
flare_blitz = move('flare blitz', 120, 100, 100, 'fire', 417, 'physical', 'recoil', 0.33)
acrobatics = move('acrobatics', 110, 0, 100, 'flying', 417, "physical", 'na', 0)
metal_claw = move('metal claw', 50, 10, 95, 'steel', 417, 'physical', 'atk+', 1.5)

#Triple Arrows Decidueye moves
triple_arrows = move('triple arrows', 90, 50, 100, 'fighting', 1250, 'physical', 'opp_def-', 0.66)
leaf_blade = move('leaf blade', 90, 0, 100, 'grass', 1250, 'physical', 'na', 0)
brave_bird = move('brave bird', 120, 100, 100, 'flying', 417, 'physical', 'recoil', 33)
steel_wing = move('steel wing', 70, 10, 90, 'steel', 417, 'physical', 'def+', 1.5)

#Swords Dance Decidueye moves
swords_dance = move('swords dance', 0, 100, 100, 'normal', 0, 'status', 'atk+', 2)
sucker_punch = move('sucker punch', 70, 50, 100, 'dark', 417, 'physical', 'spd+', 1.5)
trailblaze = move('trailblaze', 50, 100, 100, 'grass', 417, 'physical', 'spd+', 1.5)
close_combat = move('close combat', 120, 100, 100, 'fighting', 417, 'physical', 'defs-', 0.66)

#Curse Swampert moves
curse = move('curse', 0, 100, 100, 'ghost', 0, 'status', 'curs', 0)
water_pledge = move('water pledge', 80, 0, 100, 'water', 417, 'special', 'na', 0)
ice_punch = move('ice punch', 75, 0, 100, 'ice', 417, 'physical', 'na', 0)
earthquake = move('earthquake', 100, 0, 100, 'ground', 417, 'physical', 'na', 0)

#Defensive Swampert moves
ice_beam = move('ice beam', 90, 0, 100, 'ice', 417, 'special', 'na', 0)
surf = move('surf', 90, 0, 100, 'water', 417, 'special', 'na', 0)
life_dew = move('life dew', 0, 100, 100, 'water', 0, 'status', 'heal', 2)
amnesia = move('amnesia', 0, 100, 100, 'psychic', 0, 'status', 'spdef+', 2)

#Toolbox Togekiss moves
water_pulse = move('water pulse', 60, 0, 100, 'water', 417, 'special', 'na', 0)
shock_wave = move('shock wave', 60, 0, 100, 'electric', 417, 'special', 'na', 0)
gust = move('gust', 40, 0, 100, 'flying', 417, 'special', 'na', 0)

#Tank Togekiss moves
charm = move('charm', 0, 100, 100, 'fairy', 417, 'status', 'opp_atk-', 0.5)
shadow_ball = move('shadow ball', 80, 20, 100, 'ghost', 417, 'special', 'na', 0)
magical_leaf = move('magical leaf', 60, 0, 100, 'grass', 417, 'special', 'na', 0)

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
