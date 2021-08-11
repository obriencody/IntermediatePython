#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/11/2021
Purpose: Create a Recaman series: https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence
"""

import sys
from itertools import count, islice


def sequence():
    """Recaman sequence:
       a_0 = 0,
       a_n = a_(n-1) - n : if result is positive and  not already in the sequence,
       a_n = a_(n-1) + n : otherwise
    """
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a+n
        a = c


def write_sequence(filename, num):
    """
    Write the Racaman series
    :param filename: file name
    :param num: maximum number to write
    :return: nothing
    """
    with open(filename, mode='wt', encoding='utf-8') as f:
    # Generate list and Write list
    # f.writelines('{0}\n'.format(r)
    #              for r in islice(sequence(), num + 1))
        f.writelines(f'{r}\n' for r in islice(sequence(), num + 1))
    # f.close()   # remove if using 'with'

def read_series(filename):
    # f = open(filename, mode='rt', encoding='utf-8')
    # series = []
    # for line in f:
    #     series.append(int(line.strip()))
    # f.close()
    # return series

    # cleaner and closes the files for you
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


# --------------------------------------------------
def main():
    """Make your noise here"""
    write_sequence("recaman.txt", 100)
    l = read_series('recaman.txt')
    print(l)


# --------------------------------------------------
if __name__ == '__main__':
    main()
