#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""
from pprint import pp

def trace(f, *args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
    result = f(*args, **kwargs)
    print(f'result = {result}')
    return result


def test_trace():
    print(int("ff", base=16))
    trace(int, "ff", base=16)

def test_tables():
    # Use built-in zip
    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 16, 20, 21, 22, 22, 21, 19, 18, 16]
    tuesday = [12, 13, 14, 16, 20, 20, 21, 20, 19, 16, 14, 12]

    daily = [sunday, monday, tuesday]
    pp(daily)

    for item in zip(*daily):
        print(item)

    # Create a list of tuples
    transposed = list(zip(*daily))
    pp(transposed)


# --------------------------------------------------
def main():
    """Make your noise here"""
    # test_trace()
    test_tables()

# --------------------------------------------------
if __name__ == '__main__':
    main()
