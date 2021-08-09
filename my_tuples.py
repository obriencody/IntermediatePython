#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/9/2021
Purpose: Review Tuples
"""


def minmax(items):
    """
    Return the maximum and minimum of the collection
    :param items: collection of objects
    :return: min and max
    """
    return min(items), max(items)

def main():
    """
    :return:
    """
    # A tuple of any kind of object
    t = ("Ogden", 1.99, 2, 265e10)
    t = "Ogden", 1.99, 2, 265e10  # optional parenthesis
    print(t) # all tuple
    print(type(t[0])) # type of object object
    print(t[0])  # positional object
    print(f'Tuple is {len(t)} items long')

    # iterate over tuple
    for item in t:
        print(f'Item {item}')

    # concatenate
    t2 = t * 3
    for item in t2:
        print(f'item {item}')

    # nested tuples
    a = ((1, 2), (10, 20), (100, 200))
    print(a[2][0])

    for l1 in a:
        for l2 in l1:
            print(f'Item 2 {l2}')

# --------------------------------------------------
if __name__ == '__main__':
    # main()
    items = (3, 88, 11, 22, 90)
    lower, upper = minmax(items)
    print(f'minimum {lower} and maximum {upper}')
    # Test for membership: in, not in
    if 3 in items:
        print("I have a 3")
    if 99 in items:
        print("I do not have 99")
    # print(minmax(items))