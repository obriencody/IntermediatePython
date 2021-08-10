#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

def combine(size, color, animal):
    return f'{size} {color} {animal}'

# --------------------------------------------------
def main():
    """"""
    # Map() is lazy. It only produces the values as they are needed
    # ord: unicode value
    m = map(ord, 'The purple Weber State')
    print(m)
    print(next(m))
    print(next(m))
    print(next(m))
    print(next(m))
    print(next(m))
    # print(list(m))  # all elements
    print(list(map(ord, "The purple Weber State")))

    # or use a loop
    for o in map(ord, 'The purple Weber State'):
        print(o)

    sizes = ['small', 'medium', 'large']
    colors = ['green', 'blue', 'red']
    animals = ['cow', 'dog', 'cat']
    # Create a list from a map
    print(list(map(combine, sizes, colors, animals)))
    # Comprehension
    print([str(i) for i in range(5)])
    # Map
    print(list(map(str, range(5))))
    # Generator
    print(list(str(i) for i in range(5)))
    # Map
    print(list(map(str, range(5))))

# --------------------------------------------------
if __name__ == '__main__':
    main()
