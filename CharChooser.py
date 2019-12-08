#create a basic character by choosing an option and passing a dictionary to a class

import random
import time
import json

with open('entities.json') as file:
    data = json.load(file)

BASECHARS = data['BASECHARS']

MONSTERS = data['MONSTERS']


DICE = ('Sword','Sword','Sword','Shield','Shield','Skull')

class Creation(object):
    def __init__(self,Object):
        self.Type = Object['type']
        self.Name = Object['name']
        self.Attack = Object['attack']
        self.Defend = Object['defend']
        self.Move = Object['move']
        self.Mind = Object['mind']
        self.Body = Object['body']

def DiceRoller(numdice):
        myrolls=[]
        if numdice in (1,2,3,4,5):
                for roll in range(0,numdice):
                        myrolls.append(random.choice(DICE))
        else:
                print("Please, numbers 1-5 only: ",numdice)

        return myrolls


def CombatRoller(attacker,defender):
    attroll = DiceRoller(attacker.Attack)
    defroll = DiceRoller(defender.Defend)
    if defender.Type == "Player":
        defense = "Shield"
    else:
        defense = "Skull"
    print("The ",attacker.Name," attacks the ",defender.Name)
    print("Attack: ",attroll, ", Score: ",attroll.count("Sword"))
    print("Defend: ",defroll, ", Score: ",defroll.count(defense))
    if attroll.count("Sword") > defroll.count(defense):
        print("The ",defender.Name," has been wounded\n")
        defender.Body-=1
    else:
        print("The ",defender.Name," protects themself\n")

def choose_char():
    charInput = ''

    while charInput not in list(BASECHARS.keys()):
        charInput = input("Pick your character (b/w/e/d): ")
        if BASECHARS.get(charInput):
            myChar = Creation(BASECHARS[charInput])
            print(vars(myChar))
        else:
            print("You didnt pick a valid option")
    return myChar

monsterList = list(MONSTERS.keys())
monstersKilled=0

myChar = choose_char()

while myChar.Body>0:
    currMonster = Creation(MONSTERS[random.choice(monsterList)])
    print(vars(currMonster))
    time.sleep(2)
    currentRound = 1

    while myChar.Body > 0 and currMonster.Body > 0:
        print("Round: ",str(currentRound)," ,",currMonster.Name)
        if currentRound%2==1:
            CombatRoller(myChar,currMonster)
        else:
            CombatRoller(currMonster,myChar)
        currentRound+=1
        print(myChar.Name," Health: ",myChar.Body)
        if currMonster.Body == 0:
            monstersKilled+=1

input("Press enter to see final results:\n")
print("The ",myChar.Name," ended the fights with ",str(myChar.Body)," body and killed a total of ",monstersKilled," monsters")
exit()
