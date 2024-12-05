''' 
    Name: Snowball-Mania
    Author: joshua s
    Date: 12/3/24
    Class: AP Computer Science Principles
    Python: 3.13.0                 
'''
import random
import time

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


    mode = input(" Yo you  wnat to pick who you through it at yes or no?")

    gameplay(name, players, mode)

    
  


def gameplay(name, players, manual):

      while (len(players) > 1):
    
        thrower = random.choice(players)
        if(thrower == name ):
            if( manual == "yes"):
                target = input("who do you want toss at? ")
                while (target == thrower):
                     target = input ( " you picked you get some one new ")

                 


            else:        #auto mode
                    target = random.choice (players)

                    while (target == thrower):
                        target = random.choice (players)
        else:        #auto mode
                    target = random.choice (players)

                    while (target == thrower):
                        target = random.choice (players)
        print ( thrower + " is throwing a snow ball at " + target + "!")
        print (" -- ")
        print("-  -")
        print(" -- ")
        
        hitnum = random.randrange(6)

        success = hitResult(hitnum)

        time.sleep (2)

        if ( success == True):
            
            if ( target not in players):
                 print ( " you hit a passer by you are now out!!")
                 players.remove(thrower)
            print("it is a hit ! " + target + " is down")
            players.remove(target)
        else:
            print("sadly, " + thrower + " has bad aim and missed!")
      print (players[0] + " is the best snowballer is in all the land!!!!!!")

def hitResult(hitNum):
    
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if(hitNum == 3):
        return True # 1 in 5 chance some picked 3 
    return False

main()
