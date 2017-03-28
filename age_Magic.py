#!/usr/bin/env python

#########################################
# MAGIC AGE CALCULATOR
# A script to print fun facts and
# calculations based on the user's
# provided date of birth.
# Demonstrates input validation,
# arrays, and arithmetic.
# By Ku3nsting
# March, 7, 2017
#########################################

import types
import datetime

now = datetime.datetime.now()

#***********************************
# Header-printing function
#***********************************
def headerPrint():
        print "\n"
        print "-+------------------------------------+-"
        print " |             Age Magic!             |"
        print "-+------------------------------------+-"
        print " | Input your birth date, and the     |"
        print " | program will display facts and     |"
        print " | calculations relevant to your age. |"
        print "-+------------------------------------+-"

#***********************************
# Input validation function:
# Loops for more input if user-
# supplied values are invalid.
#***********************************
def validate_ints(number, upper):
        while True:
                number = input()
                try:
                        number = int(number)
                except ValueError:
                        print "Invalid Input. Please try again:\n"
                        continue

                if (0 < number and number <= upper):
                        return number
                else:
                        print "Invalid Input. Please try again:\n"
                        continue

#***********************************
# MAIN PROGRAM BODY:
#***********************************

keepGoing = True

while (keepGoing == True):

        #-----------------------------
        #PRINT THE HEADER:
        #-----------------------------
        headerPrint()


        #----------------------------------
        #GET DAY, YEAR AND MONTH FROM USER:
        #----------------------------------

        month = 0
        print ("  What month were you born? \n  Input as an integer (e.g. 7):")
        month = validate_ints(month, 12)

        day = 0
        print ("  What day were you born? \n  Input as an integer (e.g. 4):")
        day = validate_ints(day, 31)

        year = 0
        print ("  What year were you born? \n  Input as an integer (e.g. 1776):")
        year = validate_ints(year, 5000)

        #-----------------------------
        #CALCULATE AND PRINT THE OUTPUT
        #-----------------------------
        #output strings:
        monthArray= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        monthString = monthArray[month-1]

        #current Age
        age = now.year
        age = age - year
        monthAge = now.month - month
        if (monthAge < 0):
                age = age -1
        if (monthAge == 0):
                dayAge = now.date
                dayAge = dayAge - day
                if (dayAge < 1):
                        age = age -1
                if (dayAge == 0):
                        print "Today is your Birthday!"

        print "\n-+-----------------------------------+-"
        print   " |              RESULTS              |"
        print   "-+-----------------------------------+-"
        print "\nYou are currently ", age, " years old"

        #Date of 100th birthday
        hundredYear = year + 100
        print "You will turn 100 years old on:",monthString,day,hundredYear

        #Days old
        ageTo2016 = (2016 - year)-1             #total completed full years to 2016
        addLeapDays = (ageTo2016) / 4               #completed years/4 = leap years
        ageTo2016 = ageTo2016 * 365             #completed years * 365 = base days

        month2016Age = 0
        monthDaysArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        num = month - 1
        #add days in completed months beyond completed years
        for index in range(num):
                month2016Age = month2016Age + monthDaysArr[index]
        #subtract birth month, since it is only partially completed
        #must be done this way to avoid invalid index for edge cases
        month2016Age = month2016Age - monthDaysArr[month - 1]
        
        #add days in completed months before first new year
        for index in range(num, 12):
                month2016Age = month2016Age + monthDaysArr[index]

        #completed years + completed month days
        ageTo2016 = ageTo2016 + month2016Age

        #get years elapsed after 2016
        modernYears = now.year - 2016
        #add modern completed years to total
        ageTo2016 = (ageTo2016 + ((modernYears) * 365))

        if (modernYears >= 4):
                addLeapDays = addLeapDays + (modernYears / 4)

        ageTo2016 = ageTo2016 + addLeapDays    #add final leap days to total days

        #subtract days of month after today
        subMonthDays = monthDaysArr[now.month - 1] - now.day
        ageTo2016 = ageTo2016 - subMonthDays

        #subtract days of month before birth
        birthMonthDays = day - 1
        ageTo2016 = ageTo2016 - birthMonthDays

        print "You are {} days old today".format(ageTo2016)
        print "Today is your {}th day of life".format(ageTo2016 + 1)

        #Birthstone
        stoneArray= ["Garnet", "Amethyst", "Aquamarine", "Diamond", "Emerald", "Pearl", "Ruby", "Peridot", "Sapphire", "Opal", "Citrine", "Blue Topaz"]
        print "Your birthstone is: ", stoneArray[month-1]

        #Birth flower
        flowerArray = ["Carnation",
                       "Violet and Iris",
                       "Daffodil",
                       "SweetPea and Daisy",
                       "Lily of the Valley",
                       "Rose", "Larkspur",
                       "Gladiolus",
                       "Aster and Forget-me-not",
                       "Marigold",
                       "Chrysanthemum",
                       "Poinsettia"]
        print "Your birth month flower is: ", flowerArray[month-1]

        print "\n-+-----------------------------------+-"
        print   " |                END                |"
        print   "-+-----------------------------------+-"

        #-----------------------------
        # ASK USER WHETHER TO CONTINUE
        #-----------------------------
        print "\nWould you like to generate values for a new date?"
        print "1. \tYes"
        print "2. \tNo\n"
        print "Input your selection, then press ENTER:\n"
        keepGoing = validate_ints(keepGoing, 2);

print "Thanks for using Age Magic!"
print "\n"
