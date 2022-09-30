import random

print("willcome to the RCH game by serry sibaee")

z = 1

while z == 1 :
    x = int(input("choose rock by 1 \n choose ceaser by 2 \n choose hand by 3  \n if you want to leave put 4 \n" ))
    y = random.randint(1,3)
    if x == y :
        print("we draw ")
    if x == 1 and y == 2 :
        print("you win")
    if x == 1 and y == 3 :
        print("you lose")
    if x == 2 and y == 1 :
        print("you lose ")
    if x == 2 and y == 3 :
        print("you won")
    if x == 3 and y == 2 :
        print("you lose")
    if x == 1 and y == 1:
        print("you win")
    else :
        break
    z == 1
    
print ("thank you for playing ")
##    
##from random import randint
##
###create a list of play options
##t = ["Rock", "Paper", "Scissors"]
##
###assign a random play to the computer
##computer = t[randint(0,2)]
##
###set player to False
##player = False
##
##while player == False:
###set player to True
##    player = input("Rock, Paper, Scissors?")
##    if player == computer:
##        print("Tie!")
##    elif player == "Rock":
##        if computer == "Paper":
##            print("You lose!", computer, "covers", player)
##        else:
##            print("You win!", player, "smashes", computer)
##    elif player == "Paper":
##        if computer == "Scissors":
##            print("You lose!", computer, "cut", player)
##        else:
##            print("You win!", player, "covers", computer)
##    elif player == "Scissors":
##        if computer == "Rock":
##            print("You lose...", computer, "smashes", player)
##        else:
##            print("You win!", player, "cut", computer)
##    else:
##        break
##    #player was set to True, but we want it to be False so the loop continues
##    player = False
##    computer = t[randint(0,2)]
##    if player == 4 :
##        player == True

