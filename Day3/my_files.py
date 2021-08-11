#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/11/2021
Purpose: Working with files
"""

import sys


# --------------------------------------------------
def main():
    """Make your noise here"""
    print(sys.getdefaultencoding())

    # Writing text files
    # any time you open, close!!!!
    f = open('wasteland.txt', mode='wt', encoding='utf-8')  # wt = writing text
    f.write('This is the first line of the wastelands file\n')
    f.write('But, I can write more lines if I need\n to do it.\n')
    print(type(f))

    f.close()
    # Reading files
    g = open('wasteland.txt', mode='rt', encoding='utf-8')
    info = g.read()  # read 27 bytes
    print(info)
    # info = g.read()  # read the rest
    info = g.readlines()  # read all lines
    print(f'{info}')
    g.close()

    # Appending text to files
    f = open('wasteland.txt', mode='at', encoding='utf-8')  # wt = writing text
    f.writelines(['Son of man\n',
                  'You cannot say, or guess,',
                  ' for you know only\n',
                  'This is the end!\n'])

    f.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
