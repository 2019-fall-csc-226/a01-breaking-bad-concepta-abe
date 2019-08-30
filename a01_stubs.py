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
    arrOfSigns = ["Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon"]
    if passThisAlong == 1:
        for i in range(2001, 2013):
            if year == i:
                print("You are a: " + arrOfSigns[i - 2001])
    else:
        for i in range(2001, 2013):
            if year == i:
                print("Your friend is a: " + arrOfSigns[i - 2001])

def isYearInRange(year, passThisAlong):
    if passThisAlong == 1:
        if year < 2001 or year > 2012:
            print("Sorry, you must be born between 2001 and 2012...")
            print("Try again...")
            askQuestion(1)
        else:
            findSign(year, 1)
    else:
        if year < 2001 or year > 2012:
            print("Sorry, your friend must be born between 2001 and 2012...")
            print("Try again...")
            askQuestion(2)
        else:
            findSign(year, 2)

def askQuestion(passThisAlong):
    if passThisAlong == 1:
        birthYear = int(input("What year were you born in?"))
        isYearInRange(birthYear, passThisAlong)
    else:
        birthYear = int(input("What year was your friend born in?"))
        isYearInRange(birthYear, 2)

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
