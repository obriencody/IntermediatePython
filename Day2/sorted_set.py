#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/10/2021
Purpose: Sorted Set Class
"""


class SortedSet:
    def __init__(self, items=None):

        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        """Length Protocol"""
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

# --------------------------------------------------
def main():
    """Sort the set"""
    pass


# --------------------------------------------------
if __name__ == '__main__':
    main()
