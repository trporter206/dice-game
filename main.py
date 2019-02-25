import random
import os

dice_sides = 6
dice = range(1,dice_sides)

def roll_dice():
    return random.choice(dice)

def first_to_helper(scores, target):
    print scores
    diffs = [0]*len(scores)
    for index, s in enumerate(scores):
        if s is target:
            print('player '+str(index+1)+' wins!')
            break
        elif s < target:
            diffs[index] = None
        else:
            diffs[index] = s-target
    print('player '+str(diffs.index(min(x for x in diffs if x is not None))+1)+' wins!'+'\n')
    interface()

def first_to(players,target,max_rounds=50):
    os.system('clear')
    scores = [0]*players
    for i in range(1,max_rounds):
        print(' ')
        print('round '+str(i))
        for index, s in enumerate(scores, start=1):
            scores[index-1]+= roll_dice()
            print('player '+str(index)+' score: '+str(s))
        if any(i >= target for i in scores):
            first_to_helper(scores, target)
            break

def twenty_one_helper():
    return 45

def twenty_one(players):
    scores = [0]*players
    for i in range(1,players):
        scores[i-1] = twenty_one_helper()
        print('player '+str(i)+' score: '+str(scores[i-1]))
    print('player '+str(scores.index(min(x for x in scores if x is not None))+1)+' wins!'+'\n')
    interface()

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
            print(str(roll_dice())+'\n')
            interface()
        elif choice == 2:
            print "1: first to"
            print "2: 21"
            print "3: game3"
            print "4: back"
            game = input("what game?: ")

            if game == 1:
                players = input("number of players: ")
                target = input("target number: ")
                first_to(players,target)
            elif game == 2:
                players = input("number of players: ")
                twenty_one(players)
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
            print("invalid choice"+'\n')
            interface()
    choose()


interface()
