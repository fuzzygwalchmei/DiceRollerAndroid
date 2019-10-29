from random import randint
import re

diceRegex = r'[\d]+d[\d]+'
modRegex = r'[+-]\s?\d+\b'

def strip_regex(regex, string):
    """
    Takes a regex string and a text string.
    Returns a list of items found matching the regex string
    """
    return re.findall(regex, string)

def roll_dice(number=1, dice=6):
    """
    Takes 2 values. The number of dice to be rolled (defaults to 1),
    as well as the type of dice to be rolled (as a number)
    """
    return [randint(1,dice) for n in range(number)]

def split_dice(diceInput):
    """
    Takes the original string, and uses the strip regex to get all of the dice strings,
    and then splits those strings into number of dice and type of dice and returns
    a list of 2 element lists
    """
    return [re.split('[d D]',dice) for dice in strip_regex(diceRegex, diceInput)]

def dice_main(diceInput):
    """
    Main input. Takes a single string for dice and modifiers, eg. 3d6 + 5
    Uses other functions to strip out dice and roll them. Saves as a list of lists
    Uses other functions to store the modifiers as a list
    returns a dict of original string, rolls, modifiers and the total of the roll
    """
    rolls = [roll_dice(int(x),int(y)) for [x,y] in split_dice(diceInput)]
    mods = [int(mod.replace(" ","")) for mod in strip_regex(modRegex,diceInput)]
    return {'dice_string': diceInput, 'rolls':rolls, 'mods': mods, 'total': sum(sum(rolls, []), sum(mods))}
