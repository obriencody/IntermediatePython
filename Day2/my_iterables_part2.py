#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

# --------------------------------------------------
def main():
    """Make your noise here"""

    # List Comprehensions: [expr(item) for item in iterable]

    # Set Comprehensions: {expr(item) for item in iterable}
    # set is a unique list with no particular order
    s = {i for i in range(10)}
    print(s)

    # Dict Comprehensions: {key_expr: value_expr for item in iterable}
    d = {i: i*2 for i in range(10)}
    print(d)

    # Comprehensions: (item for item in iterable)
    g = (i for i in range(10))
    print(g)

    # Multiple If-Clauses
    points = []
    for x in range(5):
        for y in range(3):
            points.append((x, y))
    print(points)

    # List Comprehension
    points = [(x, y) for x in range(5) for y in range(3)]
    print(points)

# --------------------------------------------------
if __name__ == '__main__':
    main()
