import pytest
import Dice_Roller

def test_roll_dice():
    assert len(Dice_Roller.roll_dice(3,6)) == 3
    assert max(Dice_Roller.roll_dice(20,6)) <= 6
    assert min(Dice_Roller.roll_dice(20,6)) >= 1

def test_strip_regex():
    diceRegex = r'[\d]+d[\d]+'
    modRegex = r'[+-]\s?\d+\b'
    assert len(Dice_Roller.strip_regex(diceRegex,'3d6 + 2d10')) == 2
    assert Dice_Roller.strip_regex(diceRegex,'3d6 + 2d10')[0] == '3d6'
    assert Dice_Roller.strip_regex(diceRegex,'3d6 + 2d10')[1] == '2d10'

def test_split_dice():
    assert len(Dice_Roller.split_dice('3d6 + 2d10')) == 2
    assert Dice_Roller.split_dice('3d6-4 + 2d10 + 5')[0] == ['3','6']
    assert Dice_Roller.split_dice('3d6+5 + 2d10 - 4')[1] == ['2','10']

def test_dice_main():
    results = Dice_Roller.dice_main('3d6-5 + 4 +3d8')
    results['total'] >= 5
    results['total'] <= 41
    results['mods'] == [-5, 4]
    len(results['rolls']) == 2