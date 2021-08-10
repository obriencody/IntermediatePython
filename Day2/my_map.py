#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

# --------------------------------------------------
def main():
    """"""
    # Map() is lazy. It only produces the values as they are needed
    m = map(ord, 'The purple Weber State')
    print(m)


# --------------------------------------------------
if __name__ == '__main__':
    main()
