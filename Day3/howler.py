#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""

import argparse
import os


# --------------------------------------------------
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-case input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--output',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()
    # Check if string is a file
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    # str_arg = args.text
    out_fh = open(args.output, mode='wt', encoding='utf-8') if args.output else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()
    print('Done')

# --------------------------------------------------
if __name__ == '__main__':
    main()
