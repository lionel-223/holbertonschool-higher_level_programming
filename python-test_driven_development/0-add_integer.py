#!/usr/bin/python3
"""
This module supplies one function, add_integer(). For example,

>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
    ...
TypeError: b must be an integer
>>> add_integer(None)
Traceback (most recent call last):
    ...
TypeError: a must be an integer
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting them to integers).

    Arguments:
    a -- the first number
    b -- the second number (default 98)

    Returns:
    The integer sum of a and b.

    Raises:
    TypeError -- if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a)+int(b)
