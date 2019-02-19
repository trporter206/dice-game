import random

dice = [1,2,3,4,5,6]

def roll_dice():
    return random.choice(dice)

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
            return 0
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
