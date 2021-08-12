#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/11/2021
Purpose: Discuss positional and key word arguments
"""


def hyper_volume(length, *lengths):
    i = iter(lengths)
    v = length
    for item in i:
        v *= length
    return v


def tag(name, **attributes):
    """Arbitrary number of Keyword arguments,
    Use the **
    """
    # print(name)
    # print(attributes)
    # print(type(attributes))
    result = '<' + name
    # Task add info from attributes
    for key, value in attributes.items():
        result += f'{key}="{str(value)}", '
    result += '>'

    return result


def test_tag():
    print(tag('img', src='monet.jpg',
        alt='Somewhere in Europe',
        border=1))


# --------------------------------------------------
def main():
    """Make your noise here"""
    # print(hyper_volume(3, 4))
    # print(hyper_volume(3, 4, 5, 6))
    # print(hyper_volume(3))
    test_tag()



# --------------------------------------------------
if __name__ == '__main__':
    main()
