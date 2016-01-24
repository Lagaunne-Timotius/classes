# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
   if name=="rock":
    name=0    
    return name
   elif name=="spock":
        name=1
        return name
   elif name=="paper":
        name=2
        return name
   elif name=="lizard":
        name=3
        return name
   elif name=="scissor":
        name=4
        return name



    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
   if number==0:
        number="rock"    
        return number
   elif number==1:
        number="spock"
        return number
   elif number==2:
        number="paper"
        return number
   elif number==3:
        number="lizard"
        return number
   else :
        number="scissor"
        return number

    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print " "
    print "Player choose", player_choice
    player_number=name_to_number(player_choice)
    import random
    comp_number=int(random.randrange(0,4))
    comp_choice=number_to_name(comp_number)
    print "Computer choose", comp_choice
    difference=(comp_number-player_number)%5
    print comp_number,player_number,difference
    if difference>2:
       print "Computer win!"
    else:
        print "Computer lose!"
        
        
        
        
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissor")

# always remember to check your completed program against the grading rubric


