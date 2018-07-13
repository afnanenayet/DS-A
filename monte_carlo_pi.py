"""
The area of a circle is defined as $$ pi * r^2 $$. Estimate the area of a
circle using the monte carlo method.

Hint: a circle can be defined as $$ x^2 + y^2 = r^2 $$
"""

from random import random
from math import sqrt


def circle_area(radius: int) -> float:
    """ estimate the area of a circle using the monte carlo method.
    Note that the decimal precision is log(n). So if you want a precision of
    three decimal points, n should be $$ 10 ^ 3 $$.
    :param r (int): the radius of the circle
    :return (int): the estimated area of the circle to three decimal places
    """
    hits = 0
    n = 1000
    left_bottom = -1 * radius
    right_top = radius

    for _ in range(n):
        # get random coordinates
        x = left_bottom + (random() * right_top)
        y = left_bottom + (random() * right_top)

        # check if points fall within the bounds of the circle (geometrically)
        if sqrt((x ** 2) + (y ** 2)) < radius:
            hits += 1
    return (hits / n) * ((2 * radius) ** 2)


def main():
    """ wrapper for main function
    """
    area = circle_area(1)
    print(area)


if __name__ == "__main__":
    main()
