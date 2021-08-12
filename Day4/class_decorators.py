#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/12/2021
Purpose: Class as decorators
"""


class DecoratedClass(object):
    def __init__(self, original_function):
        self._original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'Call method executed this before {self._original_function.__name__}')
        return self._original_function(*args, **kwargs)


@DecoratedClass
def display():
    print('Display ran')


@DecoratedClass
def display_info(name, age):
    print(f'Display ran for {name} {age}')


# --------------------------------------------------
def main():
    """Make your noise here"""
    display()
    display_info('cody', 27)


# --------------------------------------------------
if __name__ == '__main__':
    main()
