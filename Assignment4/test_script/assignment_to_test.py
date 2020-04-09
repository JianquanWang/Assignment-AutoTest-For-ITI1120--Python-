# copy code to here

# COPYRIGHT 2020, Mohammad Alja'Afreh. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

# O(n) solution
def largest_34(a):
    '''(list)->number
    Precondition: len(a)>=4'''

    # Do not sort as it costs you n*log n.
    # Also you should copy a
    copy = a[:]
    m1 = max(copy)  # n operations
    copy.remove(m1)  # n operations
    m2 = max(copy)  # n operations
    copy.remove(m2)  # n operations
    m3 = max(copy)  # n operations
    copy.remove(m3)  # n operations
    m4 = max(copy)  # n operations

    return m3 + m4


# print(largest_34([1000, 1, 100, 2, 99, 200, -100]))

# O(n log n) solution
def largest_third(a):
    '''(list)->number
    Precondition: len(a)>=3'''
    n = len(a)
    asor = sorted(a)  # O(n log n)
    top_third_sum = 0
    for i in range(n - n // 3, n):
        print("i=", i)
        top_third_sum = top_third_sum + asor[i]
    return top_third_sum


# O(n log n) solution
def largest_third_v2(a):
    '''(list)->number
    Precondition: len(a)>=3'''
    asor = sorted(a)  # O(n log n)
    return sum(asor[-(len(a) // 3):])  # O(n)


# O(n log n)
def third_at_least(a):
    '''(list)->number
    Precondition len(a)>3'''
    asor = sorted(a)  # O(n log n)
    candidate1 = asor[len(asor) // 3]  # O(1)
    candidate2 = asor[-(len(asor) // 3 + 1)]  # O(1)
    # or equivalently if you want to avoid negative index:
    # candidate2=asor[len(asor)-(len(asor)//3+1)] #O(1)

    if asor.count(candidate1) >= len(asor) // 3 + 1:  # O(1)
        return candidate1  # O(1)
    if asor.count(candidate2) >= len(asor) // 3 + 1:  # O(1)
        return candidate2  # O(1)


##print(third_at_least([0,1,2,3,4,4,4]))


# quadratic alg, O(n^2)
def sum_tri(a, x):
    '''(list, number)->number'''
    sq = []
    # the next 3 lines do roughly O(n^2) operations
    for i in range(len(a)):
        for j in range(len(a)):
            sq.append(a[i] + a[j])

    sqs = set(sq)  # this returns a set version of sq, i.e. a version without duplicates
    # O(n^2) randomized (since sq has n^2 elements)

    # alternatively one could have created sqs by sorting sq
    # and removed duplicates in O(n^2*log n) time since the size of sq is n^2
    # final running time would still be O(n^2 log n))

    for item in a:  # O(n) of O(nlogn if they were doing binary search)
        if x - item in sqs:  # O(1) since one can search in sets in O(1) time
            # if there were doing binary serach this one line would be O(log n)
            return True  # O(1)
    return False  # O(1)


##print(sum_tri([1, 5, 8, 2, 6,55, 90],103))
##print(sum_tri([3],9))
##print(sum_tri([-1, 1, 5, 8, 2, 6], 3))
##print(sum_tri([-10,2], -18))
##print(sum_tri([1, 1, 5, 8, 2, 6],1000))

# here is a cubic alg, O(n^3)
def sum_tri_v2(a, x):
    '''(list, number)->number'''
    sq = []
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i] + a[j] + a[k] == x:
                    return True
    return False


# COPYRIGHT 2020, Mohammad Alja'Afreh. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

class Rectangle:
    # _ is used to declare class confidential properties
    _x = 0
    _y = 0
    _width = 0
    _height = 0

    # Constructs a new Rectangle whose top-left corner is specified by the
    # given coordinates and with the given width and height.
    def __init__(self, x, y, width, height):
        if width < 0 or height < 0:
            raise ValueError()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Returns this Rectangle's height.
    def get_height(self):
        return self.height

    # Returns this Rectangle's width.
    def get_width(self):
        return self.width

    # Returns this Rectangle's x coordinate.
    def get_x(self):
        return self.x

    # Returns this Rectangle's y coordinate.
    def get_y(self):
        return self.y

    # Returns a String representation of this Rectangle, such as     # "Rectangle[x=1,y=2,width=3,height=4]".
    def __str__(self):
        return ("Rectangle[x=" + str(self.x) + ", y=" + str(self.y) + ", width=" + str(self.width) + ", height=" + str(self.height) + "]")

    # Returns whether the given coordinates lie inside this Rectangle.
    def contains(self, x, y):
        return (self.x <= x and x < self.x + self.width and self.y <= y and y < self.y + self.height)

    # Returns a new Rectangle that represents the tightest bounding box
    # that contains both this rectangle and the other rectangle.
    def union(self, rect):
        left = min(self.x, rect.x)
        top = min(self.y, rect.y)
        right = max(self.x + self.width, rect.x + rect.width)
        bottom = max(self.y + self.height, rect.y + rect.height)
        return Rectangle(left, top, right - left, bottom - top)

    # Returns a new rectangle that represents the largest rectangular region
    # completely contained within both this rectangle and the given other
    # rectangle. If the rectangles do not intersect at all, returns a rectangle
    # whose width and height are both 0.
    def intersection(self, rect):
        left = max(self.x, rect.x)
        top = max(self.y, rect.y)
        right = min(self.x + self.width, rect.x + rect.width)
        bottom = min(self.y + self.height, rect.y + rect.height)
        width = max(0, right - left)
        height = max(0, bottom - top)
        return Rectangle(left, top, width, height)

    # Bonus
    def __eq__(self, rect):
        '''Returns true id two rectangles have exactly the same state
        including their x,y, width and height'''

        return self.x == rect.x and self.y == rect.y and self.width == rect.width and self.height == rect.height

# COPYRIGHT 2020, Mohammad Alja'Afreh. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.
def overlap(s, lis):
    ''' (set, list)->set'''
    result = set()
    for el in lis:
        if el in s:
            result.add(el)
    return result
def reverse(data):
    ''' (dict->dict)  function reverse accepts a dictionary from strings to strings as a parameter and
    returns a new dictionary that is the reverse of the original.'''
    result = {}
    for key, value in data.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]
    return result
def digit_sum(n):
    '''(int)->int
    Precondition: n >=0'''
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)
def digital_root(n):
    '''(int)->int
    Precondition: n >=0'''
    if n < 10:
        return n
    digsum = digit_sum(n)
    return digital_root(digsum)
    # alternatively the last two lines can be replaced by one line:
    # return digital_root(digital_sum(n))
