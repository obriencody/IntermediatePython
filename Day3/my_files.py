#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/11/2021
Purpose: Working with files
"""
import sys


# --------------------------------------------------
def main():
    """Make your noise here"""
    print(sys.getdefaultencoding())
    # Writing text files
    f = open('wasteland.txt', mode='wt', encoding='utf-8')
    f.write('This is the first\n line of text I have here. ')
    f.write('But, I can write\n more lines if I need\n to do it.\n')
    f.close()
    # Reading files
    g = open('wasteland.txt', mode='rt', encoding='utf-8')
    info = g.read(27) # read 27 bytes
    print(f'[{info}]')
    info = g.read() # read the rest
    print(f'[{info}]')
    g.close()
    # Read ALL lines
    g = open('wasteland.txt', mode='rt', encoding='utf-8')
    info = g.readlines() # read all lines
    print(f'[{info}]')
    g.close()
    # Appending text to files
    f = open('wasteland.txt', mode='at', encoding='utf-8')
    f.writelines(['Son of man\n',
                  'You cannot say, or guess,',
                  ' for you know only\n',
                  'This is the end\n' ])
    f.close()




# --------------------------------------------------
if __name__ == '__main__':
    main()
