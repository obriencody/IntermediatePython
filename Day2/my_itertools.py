#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

from itertools import islice, count
from math import sqrt

def is_prime(x):
    """
    Returns true or false if input is a prime number
    :param x: integer
    :return: TRUE or FALSE
    """
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        return True


# --------------------------------------------------
def main():
    """Make your noise here"""
    # Task: Create a list of the first 1000 prime numbers
    # thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    # print(list(thousand_primes))

    # Use the built-ins any, all
    print(any([False, False, True]))
    print(all([False, False, True]))
    cities = ['London', 'Madrid', 'New York', 'Ogden']
    # Task: Check all members in the collection have Uppercase for the first letter
    # for index in len(cities):
    #     if cities[index][0].isupper():
    #
    # print(cities[0][0].isupper())
    print(f'The cities list is {all(city == city.title() for city in cities)} to go')


    # Use built-in zip
    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 16, 20, 21, 22, 22, 21, 19, 18, 16]
    tuesday = [12, 13, 14, 16, 20, 20, 21, 20, 19, 16, 14, 12]

    # Task: Find the min, max, and average
    # for item in zip(sunday, monday):
    for sun, mon in zip(sunday, monday):
        print(f'The average = {(sun/mon)/2.0}')
        print(sun == mon)

    for temp in zip(sunday, monday, tuesday):
        print(f'minimum = {min(temp)}, maximum = {max(temp)}, average = {sum(temp)/len(temp)}')
        print(f'minimum = {min(temp):4.1f}, maximum = {max(temp):4.1f}, average = {sum(temp) / len(temp):4.1f}')
        # print(f'minimum = {:4.1f}, maximum = {:4.1f}, average = {:4.1f}'.format(min(temp), max(temp), ...))

# --------------------------------------------------
if __name__ == '__main__':
    main()
