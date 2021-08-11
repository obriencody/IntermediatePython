#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/11/2021
Purpose: Check your code with assertions
"""


# def modulus_three(n):
#     r = n % 3
#     if r == 0:
#         print('Multiple of 3')
#     elif r == 1:
#         print('Remainder 1')
#     else:  # r == 2
#         assert r == 2, 'Remainder is not 2'
#         print('Remainder 2')


def modulus_four(n):
    r = n % 4
    if r == 0:
        print('Multiple of 4')
    elif r == 1:
        print('Remainder 1')
    elif r == 2:
        print('Remainder 2')
    elif r == 3:
        print('Remainder 3')
    else:  # never case
        assert False, 'This should never happen'

# --------------------------------------------------
def main():
    """Make your noise here"""
    # assert False, 'The condition is false'
    assert 5 > 2, 'You are in a weird universe'
    modulus_four(3)
    modulus_four(4)
    modulus_four(5)

# --------------------------------------------------
if __name__ == '__main__':
    main()
