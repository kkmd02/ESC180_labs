## Problem 1
def count_evens(L):
    '''returns the number of even integers in the list L'''
    count = 0
    element = len(L) - 1
    while element >= 0:
        if L[element] % 2 == 0:
            count += 1
        element -= 1
    return count

L = [2, 2, 1, 1, 8]
count_evens(L)


##Problem 2
def list_to_str(lis):
    ''' returns the string representation of the list lis'''
    element = 0
    string_list = []
    while element <= len(lis):
        string_list.append(element)
        element += 1
    return string_list

list0 = [1, 2, 3, 4, 5, 6]

list_to_str(list0)

## Problem 3
def lists_are_the_same(list1, list2):
    '''returns True if lists are the same'''
    element = 0
    if len(list1) == len(list2):
        while element < len(list1):
            if list1[element] == list2[element]:
                element += 1
            else:
                return False
        return True
    else:
        return False

list1 = []
list2 = []

lists_are_the_same(list1, list2)

##Problem 4
def simplify_fraction(n, m):
    '''prints simplified version of fraction'''
    highest_cd = n
    while highest_cd > 0:
        if n % highest_cd == 0 and m % highest_cd == 0:
            num = int (n / highest_cd)
            denom = int (m / highest_cd)
            return str(num) + '/' + str(denom)
        else:
            highest_cd -= 1

simplify_fraction (10, 16)

## Problem 5 This one has a problem
import math

def Leibniz(value):
    fraction = 0
    for i in range (0, value + 1):
        numerator = (-1)**i
        denom = 2 * i + 1
        fraction += (numerator / denom)
    return fraction

def pi_approx(num):
    quart_pi = Leibniz (num)
    return quart_pi * 4

def approx_pi_to(n):
    ''' returns the value needed in the Leibniz function to approximate to n digits of pi '''
    x = 0
    while int(pi_approx(x) * (10 ** (n-1))) != int(math.pi * (10 ** (n-1))):
        x += 1
    return x

pi_approx(117)