#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/11/2021
Purpose: Review Exceptions
"""
from random import randrange


def more_info():
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print(f'encoding: {e.encoding}')
        print(f'reason: {e.reason}')
        print(f'object: {e.object}')
        print(f'start: {e.start}')
        print(f'end: {e.end}')


def median(iterable):
    """
    Obtain the central value of a series.
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
        return (items[median_index] + items[median_index+1])/2.0


def test_median():
    # print(f'Median odd= {median([5, 2, 1, 4, 3])}')         # Get 3
    # print(f'Median even= {median([5, 2, 1, 4, 3, 6])}')     # Get 3.5
    # print(f'Median empty= {median([])}')     # Get error
    try:
        median([])
    except ValueError as e:
        print(f'Payload: {e.args}')
        print(f'{str(e)}')


def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    # except IndexError:  #  is a subclass of LookupError
    except LookupError:  #
        print('Handled IndexError')

    d = dict(a=65, b=33)
    try:
        value = d['x']
    # except KeyError:    # is a subclass of LookupError
    except LookupError:  #
        print('Handled KeyError')

# --------------------------------------------------
def main():
    """Make your noise here"""
    # Random number between 0-99
    number = randrange(10)
    while True:
        try:
            guess = int(input('guess number?'))
        except ValueError:
            continue
        if guess == number:
            print('You got it')
            break


# --------------------------------------------------
if __name__ == '__main__':
    # main()
    # lookups()
    # test_median()
    more_info()
