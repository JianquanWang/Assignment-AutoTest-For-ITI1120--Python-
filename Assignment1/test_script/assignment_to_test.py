###############################################
#       Question 1
###############################################
def repeat(string, n, delim):
    # making string the string entered plus the delimiter at the end

    string = string + delim

    # multiplying by the number of times

    string = string * n

    return string


# getting the string, delimiter and number of repeated times,
# as well as calling function




###############################################
#       Question 2
###############################################

def is_prime(n):
    # creating list

    factorList = []

    # looping through values numbers up the number
    # and adding the values that have a null modulus to the list. If the list
    # has only two number which should be one and itself, then the number is prime
    for i in range(1, n + 1):
        if n % i == 0:
            factorList.append(i)
        else:
            continue
    if len(factorList) == 2:
        return True

    else:
        return False

    return



###############################################
#       Question 3
###############################################

import numpy
import matplotlib.pyplot as plt


def points(x1, x2, y1, y2):
    # Exits the function if the line is vertical to prevent a divided by zero.
    if x2 - x1 == 0:
        print("The line is vertical")
        return
    # Slope of line = m
    m = (y2 - y1) / (x2 - x1)

    # Distance between two points
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    x = [x1, x2]
    y = [y1, y2]

    # plotting to prove

    plt.plot(x, y)
    plt.show()
    print("The slope of the line is ", m, )
    print("The distance between the two points is ", distance)

    return


# Getting inputs from user




###############################################
##      Question 4
###############################################

def month_apart(d1, m1, d2, m2):
    # if the difference between the two months is between 0 and 1 and the date of the month that is further along in the year is smaller
    # than the date of the month earlier on in the year, the function returns false. Ex: feb 2 and jan 3 returns false
    # If those conditions are met, the function returns true

    if 1 >= m2 - m1 >= 0 and d2 - d1 < 0:
        return False

    elif 1 >= m1 - m2 >= 0 and d1 - d2 < 0:
        return False
    else:
        return True





###############################################
#       Question 5
###############################################

def reverse_int(n):
    # Getting last digit of number

    for i in range(1, 11):
        if (n - i) % 10 == 0:
            ones = i
            n = n - i

            break

    # Getting middle digit

    for i in range(10, 101, 10):
        if (n - i) % 100 == 0:
            tens = i
            n = n - i

            break

    # Getting first digit

    n = n / 100

    # Reassembling the final number

    reverseNum = ones * 100 + tens + n

    return reverseNum


# Calling function



###############################################
##      Question 6
###############################################

def vowelCount(string):
    # Setting each variable to 0
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    # Creating for loop that counts the occurance of each of the characters

    for char in string:

        if char == "a":
            a += 1

        if char == "e":
            e += 1

        if char == "i":
            i += 1

        if char == "o":
            o += 1

        if char == "u":
            u += 1

    # Returning the occurance of each of the vowels

    return print("a, e, i, o, u appear ", a, e, i, o, u, " times respectively")


# getting string input from user as well as calling the


###############################################
##      Question 7
###############################################

def allTheSame(x, y, z):
    # if numbers have the same value, return true, otherwise, return false

    if x == y == z:
        return True

    else:
        return False


def allDifferent(x, y, z):
    # if numbers have diferent values, return true, otherwise, return false

    if x != y != z:

        return True

    else:
        return False


def sorted(x, y, z):
    # If numbers are sorted, return true. otherwise return false

    if x < y < z:
        return True

    else:
        return False


allTheSame(2, 2, 2)

allDifferent(2, 3, 4)

sorted(2, 3, 4)


###############################################
#       Question 8
###############################################

def leap(year):
    # if the modulus of year and 400 is 0, return true

    if year % 400 == 0:
        return True

    # if the modulus of year and 100 is 0, return false

    elif year % 100 == 0:
        return False

    # if the modulus of year and 4 is 0, return true

    elif year % 4 == 0:
        return True

    # if the year doesn't meet any of the above conditions, return false

    else:
        return False


# Getting ipnut from user

# Calling function




###############################################
##      Question 9
###############################################

def letter2number(grade):
    # Setting both variables to 0

    bonus = 0
    numGr = 0

    # looping a variable through grade

    for i in grade:

        # Calculating the bonus

        if i == "+":
            bonus = 0.3

        elif i == "-":
            bonus = -0.3

        # translating to number

        if i == "A":
            numGr = 4

        elif i == "B":
            numGr = 3

        elif i == "C":
            numGr = 2

        elif i == "D":
            numGr = 1

        elif i == "F":
            numGr = 0

    # Adding the bonus to the main grade

    numGr = numGr + bonus

    return numGr


# Getting input from user

# Calling func


###############################################
##      Question 10
###############################################

def is_palindrome(string):
    # Creating two lists

    stringList = []
    reversedStringList = []

    # Adding the string to both lists
    for i in string:
        stringList.append(i)
        reversedStringList.append(i)

    # Reversing one of the two lists

    reversedStringList.reverse()

    # Returning True if both lists are equal

    if stringList == reversedStringList:
        return True
    else:
        return False


# Getting input from user and calling function


###############################################
##      Question 11
###############################################

def is_nneg_float(s):
    # Making s a floating point number

    s = float(s)

    # If s is greater or equal to 0 and rounding s to 1 decimal place is equal to s, return true
    # else, return false

    if s >= 0 and round(s, 1) == s:
        return True
    else:
        return False


# getting input from user and calling function




###############################################
##      Question 12
###############################################

def rps(player1, player2):
    # if both players have the same hand, return 0

    if player1 == player2:
        return 0

    # if player1 plays R, and player 2 plays S or P, return -1, 1 respectively
    if player1 == 'R':

        if player2 == 'S':
            return -1

        if player2 == 'P':
            return 1
    # same logic as above
    if player1 == 'P':

        if player2 == 'R':
            return -1

        if player2 == 'S':
            return 1
    # same logic as above
    if player1 == 'S':

        if player2 == 'P':
            return -1

        if player2 == 'R':
            return 1


# get input and call ffunction




###############################################
##      Question 13
###############################################

def alogical(n):
    number = n
    # set the starting exponent of 2 as 1
    exp2 = 1

    # keep dividing by two as long as n is greater than 1

    while n > 1:

        n = n / (2 ** exp2)

        print(n)
        exp2 += 1

        # return the number of times n has to be divided by two for the number
        # to be smaller than 1
    else:

        return exp2


###############################################
##          Question 14
###############################################

# I really don't understand why we need two inputs for this function
def count_even_digits(number, digits):
    # Creating string for the number to loop through through
    strNumber = str(number)
    counter = 0

    # looping i through the string to find even numbers

    for i in strNumber:
        intChar = int(i)
        if intChar % 2 == 0:
            counter += 1

    # returning

    return counter


# printing


