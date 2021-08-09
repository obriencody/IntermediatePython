#!/usr/bin/env python3
"""
Author: Cody O'Brien
Purpose: Say "Hello to Waldo"
"""

# Purpose: Say "Hello to Waldo"
import argparse


def get_args():
    """
    Get the command line arguments
    :return: list of parsed arguments
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name is greet')
    return parser.parse_args()


def main():
    """
    This is where the action is
    :return: N/A
    """
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == "__main__":
    main()
# print(__name__)

# print("Hello Waldo!")
