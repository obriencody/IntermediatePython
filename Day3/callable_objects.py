#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/11/2021
Purpose: Detecting Callable Objects
"""

def is_even(num):
    return num % 2 == 0


class CallMe:
    def __call__(self):
        print("Called!")

# --------------------------------------------------
def main():
    """Make your noise here"""
    print(callable(is_even))
    # Even lambdas ara callable
    is_odd = lambda x: x % 2 == 1
    print(callable(is_odd))
    # Classes are callable
    print(callable(list))
    # Methods are callable
    print(callable(list.append))
    # User Defined classes
    call_me = CallMe()
    print(callable(call_me))




# --------------------------------------------------
if __name__ == '__main__':
    main()
