import random

dice = [1,2,3,4,5,6]

def roll_dice():
    return random.choice(dice)

print roll_dice()
