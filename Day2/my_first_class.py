#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/10/2021
Purpose: Review basics of classes
"""

from math import sqrt, pow


class Point:
    """Represents a point in a 2-D geometric coordinates"""
    def __init__(self, x=0, y=0):
        """
        Initializes that position of a new point. If they are
        not specified, the oint defaults to the origin
        :param x: x-coordinate. Default = 0
        :param y: y-coordinate. Default = 0
        """
        self._x = x  # for "private" use _
        self._y = y

    def reset(self):
        """Resets the point to the new location in 2D space"""
        self.move(0, 0)

    def move(self, x, y):
        """
        Move point to a new location in 2D space
        :param x: x-coordinate
        :param y: y-coordinate
        :return: Nothing
        """
        self._x = x  # for "private" use _
        self._y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second point
        passed as a parameter.
        This function uses Pythagorean Theorem to calculate the distance
        between two points.
        :param other_point: second object of type point
        :return: distance between two points (float)
        """
        # distance = sqrt(pow(x2 - x1) + pow(y2 - y1))
        return sqrt(pow((self._x - other_point._x), 2) + pow((self._y - other_point._y), 2))
        # return sqrt((self._x - other_point._x) ** 2 + (self._y - other_point._y) ** 2)

# --------------------------------------------------
def main():
    """Make your noise here"""
    p1 = Point()
    p2 = Point(-9,3)
    # <object>.<attribute> = <value>
    # p1._x = 5
    # p1._y = 4
    # p2._x = 3
    # p2._y = 9
    print(p1._x, p1._y)
    print(p2._x, p2._y)
    print(p2.calculate_distance(p1))
    p2.reset()  # reset values
    print(p2.calculate_distance(p1))
    p2.move(3, 3)
    assert(p2.calculate_distance(p1) ==
           p1.calculate_distance(p2))
    p1.move(2, -4)
    print(p1.calculate_distance(p2))
    print(p1.calculate_distance(p1))
    # print(p2._x, p2._y)

# --------------------------------------------------
if __name__ == '__main__':
    main()
