#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

def gen246():
    print('About to yield 2')
    yield 2
    print('About to yield 4')
    yield 4
    print('About to yield 6')
    yield 6
    print('About to return')


def gen123():
    yield 1
    yield 2
    yield 3

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('Iterable is empty')

# --------------------------------------------------
def main():
    """Review Iterators and Generators"""
    # iterable = ['Spring', 'Summer', 'Fall', 'Winter']
    # print(first(iterable))
    # print(first(iterable))
    g = gen123()
    # print(type(g))

    for v in gen123():
        print(f'Value is {v}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
