#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/12/2021
Purpose: Explore when the LEGB rule does not apply.
NOTE: LEGB rule does not apply when making new bindings
"""
import time

message = 'global'


def make_timer():
    last_call = None

    def elapsed():
        nonlocal last_call
        now = time.time()
        if last_call is None:
            last_call = now
            return None
        result = now - last_call
        last_call = now
        return result
    return elapsed  # no ()


def enclosing():
    message = 'enclosing'

    def local():
        # global message  # bring global to scope
        nonlocal message  # bring to scope
        message = 'local'

    print(f'Enclosing message {message}')
    local()
    print(f'Enclosing message {message}')

# --------------------------------------------------
def main():
    """Make your noise here"""
    # print(f'Global message {message}')
    # enclosing()
    # print(f'Global message {message}')
    t = make_timer()
    print(t())
    time.sleep(2)
    print(t())
    time.sleep(3)
    print(t())


# --------------------------------------------------
if __name__ == '__main__':
    main()
