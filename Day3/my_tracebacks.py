#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""

import math
import traceback


def inclination(dx, dy):
    if dx == 0 or dy == 0:
        raise InclinationError('Illegal input values')
    return math.degrees((math.atan(dy/dx)))


def InclinationError(Exception):
    pass


# --------------------------------------------------
def main():
    """Make your noise here"""
    # print(f'inclination of 3, 5 = {inclination(3,5)} degrees')
    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e.__traceback__)
        traceback.print_tb((e.__traceback__))
        # Don't keep references to dunder-traceback
        # beyond the scope of teh except block
        s = traceback.format_tb((e.__traceback__))
        print(s)

# --------------------------------------------------
if __name__ == '__main__':
    main()
    print('Finished')