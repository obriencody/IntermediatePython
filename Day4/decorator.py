#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/12/2021
Purpose: Basics of decorators
"""


def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function  # no () so the function isn't executed


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)  # execution of the function
    return wrapper_function


@decorator_function
def display():
    print('Display function ran')


# This will not work with the current decorator
# unless you make sure to pass all the parameters
@decorator_function
def display_info(name, age):
    print(f'Display function ran for {name} {age}')


# --------------------------------------------------
def main():
    """Make your noise here"""
    hi_func = outer_function("Hi")
    bye_func = outer_function('Bye')
    hi_func()
    bye_func()

    # without decorator
    decorated_display = decorator_function(display)
    decorated_display()

    # with decorator
    display()

    # decorator with input values
    display_info('Waldo', 21)


# --------------------------------------------------
if __name__ == '__main__':
    main()
