#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""


def enclosing():
    x = 'close over'
    def local_fun():
        print(x)
    return local_fun  # no () so we aren't invoking the function


def test_enclosing():
    lf = enclosing()
    lf()
    print(lf.__closure__)


# --------------------------------------------------
def main():
    """Make your noise here"""
    test_enclosing()


# --------------------------------------------------
if __name__ == '__main__':
    main()
