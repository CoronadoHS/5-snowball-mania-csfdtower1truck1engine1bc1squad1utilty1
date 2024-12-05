''' 
    Name: Snowball-Mania
    Author: joshua s
    Date: 12/3/24
    Class: AP Computer Science Principles
    Python: 3.13.0                 
'''
import random

def main():
    # the main runner of the game
	# welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input ("what is your name?")
    print("great to have you here," + name +"! who do you want to play against? ")
    opponent = input ()
    print (name + " vs "+ opponent)
    players = []
    players.append(name)
    players.append(opponent)
    nextplayer = ""
    while(nextplayer != "done"):
        nextplayer = input (" are there any more opponest if so tpe them one at a time or done and press enter ")
        players.append(nextplayer)
    players.remove("done")

    
    while (len(players) > 1):
    
        thrower = random.choice(players)

        target = random.choice (players)

        while (target == thrower):
            target = random.choice (players)

        print ( thrower + " is throwing a snow ball at " + target + "!")
        
        hitnum = random.randrange(6)

        success = hitResult(hitnum)

        if ( success == True):
            print("it is a hit ! " + target + " is down")
            players.remove(target)
        else:
            print("sadly, " + thrower + " has bad aim and missedj")
    print (players[0] + " is the best snowballer is in all the land!!!!!!")
def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if(hitNum == 3):
        return True # 1 in 5 chance some picked 3 
    return False

main()
