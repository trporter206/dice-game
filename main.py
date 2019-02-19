import random

dice_sides = 6
dice = range(dice_sides)

def roll_dice():
    return random.choice(dice)

def dice_game():
    return 0

def interface():
    print "1: roll dice once"
    print "2: play dice game"
    print "3: roll dice x times"
    print "4: exit"

    def choose():
        choice = input("enter number: ")
        if choice == 1:
            print roll_dice()
        elif choice == 2:
            dice_game()
        elif choice == 3:
            action = input("number of rolls: ")
            for i in range(action):
                print roll_dice()
        elif choice == 4:
            exit()
        else:
            print "invalid choice"
            interface()
    choose()


interface()
