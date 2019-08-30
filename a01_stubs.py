######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your name
# Username: heggens             TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
def findSign(year, passThisAlong):
    arrOfSigns = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon","Snake", "Horse", "Goat"]
    if passThisAlong == 1:
        print("You are a: " + arrOfSigns[year % 12])
    else:
        print("You're friend is a: " + arrOfSigns[year % 12])

def askQuestion(passThisAlong):
    if passThisAlong == 1:
        birthYear = int(input("What year were you born in?"))
        findSign(birthYear, passThisAlong)
    else:
        birthYear = int(input("What year was your friend born in?"))
        findSign(birthYear, 2)

askQuestion(1)
askQuestion(2)


# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples


######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
