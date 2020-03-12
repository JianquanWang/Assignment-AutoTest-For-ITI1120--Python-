
def print_factors(n):
    print('Factors of ' + str(n) + ' = ', end='')
    if n == 1:
        print(1)
    for i in range(1, n):
        if n % i == 0:
            print(i, end=' ')
    if n > 1:
        print(n)
    return n % 2 == 0


def func_input_test():
    for i in range(4):
        s = input("Enter:")
    print("Ohyeah")
    return True

def triangle(n):
    count = n * 2
    start = 1
    for i in range(n):
        print(" " * i, end="")
        for j in range(start, count):
            print(j % (10), end='')
        count -= 1
        start += 1
        print()

import math
def approxPi(error):
    ' (float) -> float returns approximation of Pi within error'
    prev = 4
    current = 4 - 4/3
    sign = 1
    i = 5
    while abs(current-prev) > error:
        prev, current = current, current + sign*4/i
        i += 2
        sign *= -1
    return current

def longest_name(names):
   longest = ""
   tie = False
   for i in range(1, names + 1):
      name = input("name #" + str(i) + "? ")
      if len(name) > len(longest):
         longest = name
         tie = False
      elif len(name) == len(longest):
         tie = True
   longest = longest[0].upper() + longest[1:].lower()
   print(longest + "'s name is the longest")
   if (tie):
      print("(There was a tie!)")

def is_fib_like(list):
    for i in range(2, len(list)):
        if (list[i] != list[i - 2] + list[i - 1]):
            return False
    return True

def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return abs(a)

############
#  Q7
############

def password():
    pw = input("Enter your password: ")
    count = (8 <= len(pw) and len(pw) <= 16)
    for i in pw:
        if i.isupper():
            count += 1
            break
    for i in pw:
        if i.islower():
            count += 1
            break
    for i in pw:
        if i.isnumeric():
            count += 1
            break
    for i in pw:
        if i == '@' or i == '#' or i == '$' or i == '%':
            count += 1
            break
    if count == 5:
        print('Great, your password meets all requirements')
    else:
        print('Try again, your password does not meet all requirements')


def encrypt_string(my_string):
    '''str -> str'''

    new_string = ''
    for ch in my_string:
        new_string = new_string + chr(ord(ch) + 5)
    return new_string


def decrypt_string(my_string):
    '''str -> str'''

    new_string = ''

    for ch in my_string:
        new_string = new_string + chr(ord(ch) - 5)

    return new_string


if __name__ == '__main__':
    print(encrypt_string("PythonITI1120G%"))