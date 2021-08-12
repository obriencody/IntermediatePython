#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/12/2021
Purpose: Explore when the LEGB rule does not apply.
NOTE: LEGB rule does not apply when making new bindings
"""
message = 'global'


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
    print(f'Global message {message}')
    enclosing()
    print(f'Global message {message}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
