# Course: ITI 1120
# Assignment number: 2
# Due date: March 7th, 2020
# Rippeyoung, Max
# 300119899


# Quetion 1
def print_factors(n):
    '''int->bool
    takes int n and prints all factors of n and returns
    True if 2 is a factor and False otherwise
    precondition: n must be a positive integer
    '''
    result = False  # return value
    print("Factors of", n, "=", end=" ")

    for i in range(1, n + 1):  # loop for check

        if (n % i == 0):  # basic check
            print(i, end=" ")

            if (i == 2):  # second check for if n is divisible by 2
                result = True

    print("\n")
    return result  # end of function


# Question 2
def triangle(size):
    '''int->
    takes int size and prints a tringle (size*2-1) wide
    and size tall of numbers
    precondition: size must be an int > 0
    '''
    width = size * 2 - 1

    for i in range(1, size + 1):  # loop for rows
        print(" " * i, end="")

        for j in range(width):  # loop for numbers in rows
            print(i + j, end="")

        width -= 2  # adjust width
        print("\n")


# Question 3
def approxPi(error):
    '''float->float
        approximates pi within error by computing sums
        4/i as i increases by 2, starting at 1, and alterating
        positive and negative. These sums are taken until the
        difference between the current sum, pi, and the previous sum, pip are
        no greater than error
    '''
    i = 1
    pi = 0
    pip = 0
    swap = 0
    while (pi - pip) < error:
        if swap == 0:
            pi += 4 / i
            swap = 1
        elif swap == 1:
            pi -= (4 / i)
            swap = 0
        i += 2
        if abs(pi - pip) > error:
            pip = float(pi)
        elif abs(pi - pip) < error:
            return pi


# Question 4
def longest_name(n):
    '''int->None
    takes number of names, n, as parameter then asks user for input
    n number of names. prints the longest name.
    '''
    curName = ''
    longName = ''
    tie = False
    for i in range(0, n):
        print("Enter Name #" + str(i + 1), end='')
        curName = input(': ')
        print('\n')
        if len(curName) > len(longName):
            longName = str(curName)
            tie = False
        elif len(curName) == len(longName):
            tie = True
    longName = longName.lower()
    longName = longName.capitalize()
    print(longName + "'s name is longest")
    if tie == True:
        print("(There was a tie!)")


# Question 5
def is_fib_like(lint):
    '''list->bool
    takes list of ints, lint, as parameter and checks if all values
    after the first two are a sum of previous two. returns true if true,
    false if false
    '''
    if len(lint) < 3:
        return True
    else:
        for i in range(0, len(lint) - 2):
            if (lint[i] + lint[i + 1]) != lint[i + 2]:
                return False
        return True


# Question 6
def gcd(a, b):
    '''(int, int)->int
    takes a and b as parameters and returns their greatest common divisor
    '''

    if (a == 0):
        print("The greatest common divisor of", a, "and", b, "is:", abs(b))
    elif (b == 0):
        print("The greatest common divisor of", a, "and", b, "is:", abs(a))
    else:
        i = 1

        while (i <= abs(a) and i <= abs(b)):
            if ((a % i) == 0 and (b % i) == 0):
                result = i
            i = i + 1
        print("The greatest common divisor of", a, "and", b, "is:", result)


# Question 7
def password():
    '''None->None
    takes a user inputted password and verifies if it meets requirements
    using a list of bools to keep track of requirements
    '''

    check = [False, False, False, False, False]
    password = input("Enter your password: ")
    if (len(password) >= 8) and (len(password) <= 16):
        check[0] = True
    for i in password:
        if i.isnumeric():
            check[3] = True
        elif (i == '@') or (i == '#') or (i == '$') or (i == '%'):
            check[4] = True
        elif i == i.upper():
            check[1] = True
        elif i == i.lower():
            check[2] = True

    if False in check:
        print("Try again, your password does not meet all requirements")
    else:
        print("Great, your password meets all requirements")


# Question 8
def encrypt_string():
    '''None->str
    takes password as input and returns an encrypted version
    '''
    result = ''
    password = input("Enter your password: ")
    for i in password:
        result = result + chr(ord(i) + 5)
    return result


# Question 9
def decrypt_string():
    '''None->str
    takes encrypted string as input and returns a decrypted version
    '''
    result = ''
    password = input("Enter encrypted string: ")
    for i in password:
        result = result + chr(ord(i) - 5)
    return result

if __name__ == '__main__':
    triangle(5)