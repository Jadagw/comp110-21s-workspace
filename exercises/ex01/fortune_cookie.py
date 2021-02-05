"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730409609"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune_number = randint(1, 100)

print("Your fortune cookie says...")

if bool(fortune_number > 50) :
    if bool(fortune_number > 75) :
        print("You will be very wealthy!")
    else :
        print("You will be very succesful!")

else :
    if bool(fortune_number > 25) :
        print("You will have lots of kids!")
    else : 
        print("You will have many cats!")

print("Now, go spread positive vibes!")

