######################################################################
# Author: Bryar Frank
#           Ben Maynard
#             Vidya Mastriyana
# Username: frankb, maynardb, mastriyanag
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

 
delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print("\n")
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West]")

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may NOT be coming right after the example above.
# Introduction
print('''Ah! So I see you're still alive ''' + username + "!")
print('''Little did you know though, you have yet another path before you!''')
print('''Before you, you see a old, green bridge. It's length is terrifying, looking as though it goes for miles''')
print('''each board creeks as a small, wrinkly figure appears before your''')
print('''It looks like a troll and begins to speak to you''')
print('''Troll: Here before you is the bridge of DEE''')
print('''       If you wish to pass, answer these questions, three''')
print('''''')
# Assign user input values
playername = input('       What ... is your name?')
print('       What ... is your quest?')
quest = input('     You say, "I seek: ')
quest = quest.lower()
color = input('       What is my favorite color?')
color = color.lower()

# Checks if player gets all questions right or all questions wrong
if playername == username and quest == "the holy grail" and color == "green":
    # Good Answer
    print("As you answer the last question you leave the troll flabergasted and he goes flying off into the sky.")
    print( "He will bother you no more and you can finnaly continue onward in your journey")
    print("plus you pick up a bag of doritos on your way")
elif playername != username and quest != "the holy grail" and color != "green":
    # Bad Answer
    print("Oh no it seems you have not meet up to the trolls standards")
    print("You feel the wind building up beneath you and within seconds you find you self launched it to the air")
    sleep(delay)

    dead = True
else:
    print("You have just barley meet the trolls standards. you may pass the bridge")
    print("he does growl at you as you pass though")
# Scott Heggen is Iron Man :) also the TA's
if dead == True:
    print("As your consciousness slowly fades, a shaded figure appears.")
    print("Before you pass, you realize that the shaded figure is Scott Heggen.")
    print('He leans over and says, "better luck programming next time." Then he takes your wallet.')
    print("It was sad, because you remember as he leaves that you had a coupon in there.")
    print("You are dead.")

    quit()



# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
