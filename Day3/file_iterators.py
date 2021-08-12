#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/11/2021
Purpose: Read text file. File names as positional parameter
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Read File',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fname',
                        metavar='str',
                        help='A file to read')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    str_arg = args.fname
    print(f'str_arg = "{str_arg}"')
    f = open(str_arg, mode='rt', encoding='utf-8')
    for line in f:
        print(line.strip())
    f.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
