######################################################################
# Author: Abraham Moreno      TODO: Change this to your name
# Username: morenoa2             TODO: Change this to your username
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

# This function takes in the person's birth year and does logic to find the person's sign.
# passThisAlong is the question. If it = 1, then it asks the first question. If not, it asks the second question.
def findSign(year, passThisAlong):
    # This is a list of all the signs
    arrOfSigns = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon","Snake", "Horse", "Goat"]
    if passThisAlong == 1:
        # This finds the remainder of the year given over 12 and chooses the sign in that place.
        print("You are a: " + arrOfSigns[year % 12])
    else:
        print("You're friend is a: " + arrOfSigns[year % 12])

# This function is used to choose which question should be called(passThisAlong). It also calls findSign with the value of birthYear.
def askQuestion(passThisAlong):
    if passThisAlong == 1:
        # Stores the value of whatever the user inputs
        # Checks to see if the value is a digit. Learned about isdigit() thanks to:
        # https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
        birthYear = input("What year were you born in?")
        if birthYear.isdigit():
            # Calls findSign with the birthYear and 1 indicating the first question.
            findSign(int(birthYear), 1)
        else:
            print("Please input a number value(2000, 2001, etc.)")
            askQuestion(1)
    else:
        birthYear = input("What year was your friend born in?")
        if birthYear.isdigit():
            findSign(int(birthYear), 2)
        else:
            print("Please input a number value(2000, 2001, etc.)")
            askQuestion(2)

# Calls the question with the question number as a parameter.
askQuestion(1)
askQuestion(2)
