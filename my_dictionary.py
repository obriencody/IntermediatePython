#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

from pprint import pprint as pp

def main():
    """Review Dictionaries"""

    urls = {'Google': "https://google.com",
            'Twitter': "https://twitter.com",
            'WSU': "https://weber.edu"}
    print(type(urls))
    print(urls)

    # curls = urls.copy()
    urls['WSU'] = 'https://weber.edu.tmp'
    print(urls)
    # to iterate over keys
    for key in urls:
        print(f'{key} => {urls[key]}')
    # to iterate over values
    for value in urls.values():
        print(f'values => {value}')
    # to iterate over items
    for key, value in urls.items():
        print(f'{key} => {value}')

    pp(urls)

# --------------------------------------------------
if __name__ == '__main__':
    main()
