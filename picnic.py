#!/usr/bin/env python3
"""
Author : t24 <codyobrien@mail.weber.edu>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',  # one or more args
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action="store_true",
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    items = list(args.item)
    print(args.item)

    # check if the list needs to be sorted
    if args.sorted:
        items.sort()

    print(items)

    # prepare list to print
    num = len(items)
    # 1 item: just print it
    if num == 1:
        bringing = items[0]
    # 2 items: item 1 and item 2
    elif num == 2:
        bringing = ' & '.join(items)
    # 3 or more items: item1, item2, item3 ...
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    # sort the input

    # Print info

    print(f'You are bringing {bringing}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
