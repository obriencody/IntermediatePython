#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/12/2021
Purpose: Learn how local functions work
"""


def fun1():
    """Regular Function"""
    x = 1
    y = 2
    return x + y


def fun2():
    """Regular Function"""
    def local_fun():
        """Local Function"""
        a = "Hello"
        b = "World"
        return a + b
    x = 1
    y = 2
    return x + y


store = []


def sort_by_last_letter(string):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(string, key=last_letter)


# LEGB rule -- Local, Enclosing, Global, Built-in
g = 'global'


def outer(p='param'):
    l = 'local'

    def inner():
        print(g, p, l)
    inner()


# --------------------------------------------------
def main():
    """Make your noise here"""
    # print(fun1())
    # print(fun2())
    # s = ['hello', 'how', 'are', 'you']
    # print(sort_by_last_letter(s))
    # print(sort_by_last_letter(s))
    # print(sort_by_last_letter(s))
    outer()


# --------------------------------------------------
if __name__ == '__main__':
    main()
