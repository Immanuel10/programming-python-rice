# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    global secret_number 
    global maximum 
    global guess_attempt
    maximum = 100
    secret_number = random.randint(0, maximum)
    guess_attempt = int(math.ceil(math.log(maximum+1,2)))
    print "Number is between 0-100"
    print "Maximum attempts is", guess_attempt
    
    
    # define event handlers for control panel
def range100():
    global secret_number 
    global maximum 
    global guess_attempt
    maximum = 100
    secret_number = random.randint(0, maximum)
    guess_attempt = int(math.ceil(math.log(maximum+1,2)))
    print "Number is between 0-100"
    print "Maximum attempts is", guess_attempt
    

def range1000():
    global secret_number 
    global maximum 
    global guess_attempt
    maximum = 1000
    secret_number = random.randint(0, maximum)
    guess_attempt = int(math.ceil(math.log(maximum+1,2)))
    print "Number is between 0-1000"
    print "Maximum attempts is", guess_attempt
    
        
def input_guess(guess):
    global guess_attempt, maximum
    guess = int(guess)
    guess_attempt -= 1
    print "Guess was", guess
    
    if guess == secret_number:
        print "Correct"
        if maximum == 100:
            range100()
        else:
            range1000()
    elif guess > secret_number:
        print "Lower"
        print "You have", guess_attempt, "remaining attemps"
    elif guess < secret_number:
        print "Higher"
        print "You have", guess_attempt, "remaining attemps"
    if guess_attempt == 0:
        print "Game over, the number was", secret_number
        print ""
        if maximum == 100:
            range100()
        else:
            range1000()     

# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)
button = frame.add_button('Range 0-100', range100, 100)
button2 = frame.add_button('Range 0-1000', range1000, 100)
button3 = frame.add_button('Reset', new_game, 100)

# register event handlers for control elements and start frame

frame.add_input('Enter a number', input_guess, 100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
