import random

dice_sides = 6
dice = range(dice_sides)

def roll_dice():
    return random.choice(dice)

def game1():
    return 0

def game2():
    return 0

def game3():
    return 0

def interface():
    print "1: roll dice once"
    print "2: play dice games"
    print "3: roll dice x times"
    print "4: exit"

    def choose():
        choice = input("enter number: ")
        if choice == 1:
            print roll_dice()
        elif choice == 2:
            print "1: game1"
            print "2: game2"
            print "3: game3"
            print "4: back"
            game = input("what game?: ")

            if game == 1:
                game1()
            elif game == 2:
                game2()
            elif game == 3:
                game3()
            elif game == 4:
                interface()
            else:
                print "invalid choice"
                interface()

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
