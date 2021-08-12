#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/12/2021
Purpose: Function Factory
"""


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp  # no ()


# --------------------------------------------------
def main():
    """Make your noise here"""
    square = raise_to(2)
    cubed = raise_to(3)
    fourth = raise_to(4)
    print(square.__closure__)
    print(square(9))
    print(cubed.__closure__)
    print(cubed(3))
    print(fourth.__closure__)
    print(fourth(2))

# --------------------------------------------------
if __name__ == '__main__':
    main()
