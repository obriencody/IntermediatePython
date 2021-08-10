#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""
def main():
    """Review Ranges"""
    r = range(5)
    print(r)
    print(type(r))
    for item in r:
        print(f'item {item}')
    # Set the upper and lower limit
    r = range(5, 10)
    for item in r:
        print(f'item {item}')
    # Create list out of ranges
    # Ranges third optional parameter is the step size
    l = list(range(0, 10, 2)) + list(range(20, 60, 3))
    print(l)
    print(type(l))
    for item in l:
        print(f'item {item}')

    # Enumerate
    t = [6, 345, 67, 99, 234]
    for i,v in enumerate(t):
        print(f'Index {i}, value {v}')
# --------------------------------------------------
if __name__ == '__main__':
    main()
