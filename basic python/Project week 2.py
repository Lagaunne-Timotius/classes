# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui

low=0
high= 100
number=7
tbg=0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global number,tbg,low,high
    tbg=random.randint(low, high)
    if high==100:
        number=7
    else:
        number=10
    print "New game. Range is from",low,  "to", high
    print "Number of remaining guesses is", number
    # remove this when you add your code    



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global high, number
    high=100
    number=7
    new_game()
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global high, number
    high=1000
    number=10
    new_game()
    
    
    
def input_guess(guess):
    # main game logic goes here	
    global number,tbg
    number=number-1
    guess=int(guess)
    print "Guess was",guess
    print "Number of remaining guesses is",number
    if number >0:
        if guess==tbg:
            print "Correct!"
            new_game()
        elif guess>tbg:
            print "Lower!"
        else: 
            print "Higher!"
    else:
        print "You ran out of guesses.  The number was",tbg
        new_game()
    # remove this when you add your code
    

    
# create frame
frame=simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
frame.add_button("range 0-100",range100,100)
frame.add_button("range 0-1000",range1000,100)
frame.add_input("guess number",input_guess,100)
frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
