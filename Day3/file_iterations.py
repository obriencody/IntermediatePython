#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/11/2021
Purpose: Read text file. File names...
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

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

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
