from random import randint
import re

diceRegex = "[\d]d[\d]"
modRegex = r'[+-]\s?\d\b'

def roll_dice(number=1, dice=6):
    return [randint(1,dice) for n in range(number)]

def getItems(diceInput):
    myDice = re.findall(diceRegex,diceInput)
    myMods = re.findall(modRegex,diceInput)
    rolls = [roll_dice(int(x),int(y)) for [x,y] in [re.split('[d D]',dice) for dice in myDice]]
    mods = [int(mod.replace(" ","")) for mod in myMods]
    return rolls, mods

print("Rolls: ",rolls) #, sum(rolls)
print("Mods: ",mods) #, sum(mods)
sumRolls = sum(list(map(sum, rolls)))
sumMods = sum(mods)
print(sumRolls + sumMods)
