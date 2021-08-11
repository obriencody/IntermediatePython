#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""

from random import randrange


def median(iterable):
    """
    Obtain the central value of a series
    Sort the iterable and return the middle value if there is an odd
    number of elements, or the arithmetic mean of the middle two elements
    if there is an even number of elements
    :param iterable: A series of iterable items
    :exception ValueError for empty sequence
    :return: The median value
    """

    if len(iterable) == 0:
        raise ValueError('median() arg is an empty sequence')

    items = sorted(iterable)
    median_index = (len(items) - 1) // 2
    if len(items) % 2 != 0:
        return items[median_index]
    else:
        return (items[median_index] + items[median_index + 1])/2.0

def test_median():
    # print(f'Median odd= {median([5, 2, 1, 4, 3])}')  # get 3
    # print(f'Median even= {median([5, 2, 1, 4, 3, 6])}')  # get 3.5
    # print(f'Median empty= {median([])}')  # get error
    try:
        median([])
    except ValueError as e:
        print('Payload: {e.args]')
        print(f'{str(e)}')

def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    # except IndexError:  # first
    except LookupError:  # first
        print('Handled IndexError')

    d = dict(a=65, b=35)
    try:
        value = d['x']
    # except KeyError: # is a subclass of lookupError
    except LookupError:  # first
        print('Handled KeyError')


# --------------------------------------------------
def main():
    """Make your noise here"""
    # Random number between 0-99
    # num = randrange(10)
    # while True:
    #     try:
    #         guess = int(input('Guess number? '))
    #     except ValueError:
    #         continue
    #     if guess == num:
    #         print('You guessed correctly, captain!')
    #         break


# --------------------------------------------------
if __name__ == '__main__':
    # main()
    # lookups()
    # Get 3
    # print(f'Median odd= {median([5, 2, 1, 4, 3])}')
    # # Get 3.5
    # print(f'Median even= {median([5, 2, 1, 4, 3, 6])}')
    test_median()