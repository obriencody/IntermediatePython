#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""


def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    """
    Print argument info
    :param arg1: First required position argument
    :param arg2: Second required position argument
    :param args: Optional list of positional arguments (LAST OF POSITIONAL)
    :param kwarg1: First required Keyword argument
    :param kwarg2: Second required Keyword argument
    :param kwargs: Optional list of Keyword argument (MUST BE LAST)
    :return: argument info
    """
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


def print_pos_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


def colors(red, blue, green, **kwargs):
    print(f'r = {red}')
    print(f'b = {blue}')
    print(f'g = {green}')
    print(kwargs)

# --------------------------------------------------
def main():
    """Make your noise here"""
    print_args(1, 2, kwarg1='hello', kwarg2='there')  # minimum to run
    print_args(1, 2, 3, 4, kwarg1='hello', kwarg2='there')
    print_args(1, 2, 3, 4,
               kwarg1='hello', kwarg2='there',
               name='Waldo', lname='Weber')  # two optional positional params

    t = (11, 22, 33, 44, 55, 66)
    # * to unpack tuple
    print_pos_args(*t)  # *t for this unpacks the tuple on the fly --
                        # so 11 is first arg, 22 is second arg, rest is the optional arg

    print_pos_args(t, t)  # passing two required positional args (two tuples in this case)
    print_pos_args(t[0], t[1], t[2:])  # this creates a new list in *args -- not what we want

    # Use dictionary
    # ** used to unpack dictionary
    k = {'red': 21, 'blue': 120, 'green': 68, 'alpha': 52}
    colors(**k)

# --------------------------------------------------
if __name__ == '__main__':
    main()
