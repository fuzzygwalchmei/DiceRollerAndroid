from random import randint
import re

diceRegex = r'[\d]+d[\d]+'
modRegex = r'[+-]\s?\d+\b'

def strip_regex(regex, string):
    return re.findall(reg, string)

def roll_dice(number=1, dice=6):
    return [randint(1,dice) for n in range(number)]

def split_dice(diceInput):
    return [re.split('[d D]',dice) for dice in strip_regex(diceRegex, diceInput)]

def getItems(diceInput):
    rolls = [roll_dice(int(x),int(y)) for [x,y] in split_dice(diceInput)]
    mods = [int(mod.replace(" ","")) for mod in strip_regex(modRegex,diceInput)]
    return {'dice_string': diceInput, 'rolls':rolls, 'mods': mods, 'total': sum(sum(rolls, []), sum(mods))}
